from django.template.response import TemplateResponse
from django.contrib.admin.options import IS_POPUP_VAR, TO_FIELD_VAR
from django.contrib.admin.utils import unquote
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from mighty.admin.models import BaseAdmin
from mighty.applications.logger import views
from functools import update_wrapper
from mighty.models import Log

class ModelWithLogAdmin(BaseAdmin):
    change_form_template  = 'admin/change_form_wlog.html'

    def logs_view(self, request, object_id, extra_context=None):
        opts = self.model._meta
        to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
        obj = self.get_object(request, unquote(object_id), to_field)
        ctype = ContentType.objects.get(app_label=obj.app_label, model=obj.model_name)
        context = {
            **self.admin_site.each_context(request),
            'object_name': str(opts.verbose_name),
            'object': obj,
            'fake': Log(),
            'logs': Log.objects.filter(content_type=ctype, object_id=obj.id),
            'opts': opts,
            'app_label': opts.app_label,
            'media': self.media
        }
        request.current_app = self.admin_site.name
        return TemplateResponse(request, 'admin/logs.html', context)

    def get_urls(self):
        from django.urls import path
        urls = super(ModelWithLogAdmin, self).get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name
        my_urls = [
            path('<path:object_id>/logs/', self.wrap(self.logs_view), name='%s_%s_logs' % info),
        ]
        return my_urls + urls

class ModelWithChangeLogAdmin(BaseAdmin):
    change_form_template  = 'admin/change_form_wlog.html'

    def logs_view(self, request, object_id, extra_context=None):
        opts = self.model._meta
        to_field = request.POST.get(TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR))
        obj = self.get_object(request, unquote(object_id), to_field)
        context = {
            **self.admin_site.each_context(request),
            'object_name': str(opts.verbose_name),
            'object': obj,
            'fake': obj.changelog_model(),
            'logs': obj.changelog_model.objects.filter(model_id=obj),
            'opts': opts,
            'app_label': opts.app_label,
            'media': self.media
        }
        request.current_app = self.admin_site.name
        return TemplateResponse(request, 'admin/change_logs.html', context)

    def get_urls(self):
        from django.urls import path
        urls = super(ModelWithChangeLogAdmin, self).get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name
        my_urls = [
            path('<path:object_id>/logs/', self.wrap(self.logs_view), name='%s_%s_logs' % info),
        ]
        return my_urls + urls