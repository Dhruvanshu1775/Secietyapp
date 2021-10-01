from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.models import User

def login_success(request, user, *args, **kwargs):
    print('-----------')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print(f'kwargs:{kwargs}')
    user_logged_in.connect(login_success, sender = User)
