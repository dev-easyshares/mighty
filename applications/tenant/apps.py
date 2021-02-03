from django.apps import AppConfig
from django.conf import settings
from mighty import over_config
from mighty.functions import setting
from django.contrib.auth import get_user_model

class Config:
    invitation_enable = True
    invitation_days = 7
    invitation_url = 'http://%(domain)s/user/tenant/%(uid)s/?token=%(token)s'

    class Default:
        group = [
            {
                'name': 'manager',
                'is_immutable': True,
            },
            {
                'name': 'comptable',
            },
            {
                'name': 'ressources humaines',
            },
            {
                'name': 'avocat',
            },
            {
                'name': 'juriste',
            },
            {
                'name': 'salarié',
            },
        ]

    class ForeignKey:
        group = setting('TENANT_GROUP', 'auth.Group')
        role = setting('TENANT_ROLE', 'mighty.Role')
        alternate = setting('TENANT_ALTERNATE', 'mighty.TenantAlternate')
        tenant = setting('TENANT_MODEL', 'mighty.Tenant')
        missive = setting('TENANT_MISSIVE', 'mighty.Missive')
        invitation = setting('TENANT_INVITATION', 'mighty.TenantInvitation')
        nationalities = setting('TENANT_NATIONALITY', 'mighty.Nationality')
        user = settings.AUTH_USER_MODEL
        optional = False

if hasattr(settings, 'TENANT'): over_config(Config, settings.TENANT)
class TenantConfig(AppConfig, Config):
    name = 'mighty.applications.tenant'

    def ready(self):
        from . import signals
