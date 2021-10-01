from django.urls import path
from .views import SecretaryView, HouseView, AssignMember, delete, GuestView, HouseGuestView, HouseGuestEdit, logout

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('secretary/', SecretaryView.as_view(), name='secretary'),
    path('house/', HouseView.as_view(), name='house'),
    path('assignmember/<slug>', AssignMember.as_view(), name='assignmember'),
    path('delete/<slug>/<int:id>', delete, name='delete'),
    path('guest/', GuestView.as_view(), name='guest'),
    path('house/<slug>', HouseGuestView.as_view(), name='houseguest'),
    path('houseedit/<slug>/<pk>', HouseGuestEdit.as_view(), name='guestedit')
]
