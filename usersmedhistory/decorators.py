from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def healthworker_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    Decorator that ensures only healthworkers can have access to a particular view or the user will
    be redirected to the homepage
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_healthworker,
        login_url='/',
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
