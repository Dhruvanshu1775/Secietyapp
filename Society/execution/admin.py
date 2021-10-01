from django.contrib import admin
from .models import HouseNo, Member, GuestCategory, Guest

# Register your models here.

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    model = Guest
    list_display = [
        'guestcategory_key',
        'house_key',
        'guest_name',
        'total_member',
    ]

@admin.register(HouseNo)
class HouseAdmin(admin.ModelAdmin):
    model = HouseNo
    list_display = [
        'number',
        'member_id',
    ]

admin.site.register(Member)
admin.site.register(GuestCategory)
