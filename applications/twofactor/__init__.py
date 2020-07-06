default_app_config = 'mighty.applications.twofactor.apps.TwofactorConfig'

from django.contrib.auth import _get_backends

def send_sms(user, phone):
    for backend, backend_path in _get_backends(return_tuples=True):
        if hasattr(backend, 'send_sms') and backend.send_sms(user, phone, backend_path):
            return True
    return False

def send_email(user, email):
    for backend, backend_path in _get_backends(return_tuples=True):
        if hasattr(backend, 'send_email') and backend.send_email(user, email, backend_path):
            return True
    return False