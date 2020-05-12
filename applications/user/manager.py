from django.contrib.auth.models import UserManager

PrefetchRelated = ('user_email', 'user_phone', 'user_ip', 'user_useragent')
class UserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('method', 'CREATESUPERUSER')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)

    def get_queryset(self):
        return super().get_queryset().prefetch_related(*PrefetchRelated)