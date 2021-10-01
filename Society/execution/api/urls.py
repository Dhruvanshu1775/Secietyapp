from django.urls import path
from .views import GuestApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guestapi', GuestApiView, basename='guestapi')
