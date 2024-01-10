from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
#from phonenumber_field.widgets import PhoneNumberPrefixWidget
#from phonenumber_field.formfields import PhoneNumberField

from mighty.applications.user import get_form_fields, translates as _
from mighty.forms import ModelFormDescriptable

from mighty.applications.user.signals import merge_accounts_signal

allfields = get_form_fields()
required = get_form_fields('required')
optional = get_form_fields('optional')

#if 'phone' in allfields:
#    class UserCreationForm(UserCreationForm):
#        phone = PhoneNumberField(label=_.phone, widget=PhoneNumberPrefixWidget(initial='FR'), required=False)

if 'password1' not in allfields:
    class UserCreationForm(UserCreationForm):
        password1 = None
        password2 = None

        def clean(self):
            self.cleaned_data["password1"] = None
            super().clean()

class UserCreationForm(UserCreationForm, ModelFormDescriptable):
    force_order = (
        "last_name",
        "first_name",
        "email",
        "phone",
        "password1",
        "password2",
        "cgu",
    )

    class UsernameField(UsernameField):
        pass

    def prepare_descriptor(self, *args, **kwargs):
        self.fields["phone"].icon = "mobile"

    class Meta:
        model = get_user_model()
        fields = allfields

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in allfields:
            if field in required:
                self.fields[field].required = True
        self.add_icon()
        self.reorder()

    def reorder(self):
        new_fields = {}
        for field in self.force_order:
            if field in self.fields:
                new_fields[field] = self.fields[field]
                del self.fields[field]
        for field, data in self.fields.items():
            new_fields[field] = data
        self.fields = new_fields

    def add_icon(self):
        if "last_name" in self.fields: self.fields["last_name"].icon = "user"
        if "first_name" in self.fields: self.fields["first_name"].icon = "user"


UserModel = get_user_model()
def get_related_field():
    class Tmp:
        name = "id"
    return Tmp
UserModel.get_related_field = get_related_field()
UserModel.model = UserModel
UserModel.limit_choices_to = {}

class UserMergeAccountsAdminForm(ModelFormDescriptable):
    account_keep = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=ForeignKeyRawIdWidget(UserModel(), admin.site),
    )
    account_delete = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=ForeignKeyRawIdWidget(UserModel(), admin.site),
    )

    class Meta:
        model = UserModel
        fields = ()

    def save_form(self):
        kp = self.cleaned_data["account_keep"]
        dl = self.cleaned_data["account_delete"]

        for data_link in ("user_email", "user_phone", "user_address"):
            try:
                getattr(dl, data_link).update(user=kp)
            except Exception:
                pass

        merge_accounts_signal.send(sender=None, tokeep=kp, todelete=dl)
        dl.delete()

