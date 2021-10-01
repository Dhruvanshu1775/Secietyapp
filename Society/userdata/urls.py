from django.urls import path
from .views import login, register, MemberPage

urlpatterns = [
    path('Login/', login, name='login'),
    path('Register/', register, name='register'),
    path('member/', MemberPage, name='member'),
]
