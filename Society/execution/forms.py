from django import forms
from .models import HouseNo, Guest

class HouseForm(forms.ModelForm):
    class Meta:
        model = HouseNo
        fields = ('number',)
        labels = {
            'number':'Enter House number',
        }


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('house_key', 'guestcategory_key',
            'guest_name','purpose','total_member','mobile_number','special_key',
        )
        labels = {
            'guest_name':'Enter Guest Name',
            'purpose':'Enter Purpose' ,
            'total_member':'Total Member' ,
            'mobile_number':'Enter Mobile Number',
        }
