from django.db import models
from django.contrib.auth.models import User
from userdata.models import UserInfo, TimeDateMixin
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_delete

# Create your models here.

class HouseNo(TimeDateMixin):
    user_key  = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True,)
    number    = models.CharField(max_length = 250)
    slug      = models.SlugField()
    member_id = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.number

    def save(self,*args,**kwargs):
        self.slug = slugify(self.number)
        super().save(*args,**kwargs)

def save_post(sender, instance, **kwargs):
    print("Data save succesfully")
post_save.connect(save_post, sender = HouseNo)

def delete_post(sender, instance, **kwargs):
    print("Data delete"+str(instance))
pre_delete.connect(delete_post, sender = HouseNo)



class Member(TimeDateMixin):
    s_key     = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'skey')
    user_key  = models.OneToOneField(User, on_delete = models.CASCADE, blank = True, null = True)
    house_key = models.ForeignKey(HouseNo, on_delete = models.CASCADE, blank = True, null = True)
    is_head   = models.BooleanField(default = False)

    def __str__(self):
        return str(self.user_key)

class GuestCategory(models.Model):
    s_key = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'skey_g')
    name  = models.CharField(max_length = 250)

    def __str__(self):
        return str(self.name)


class Guest(TimeDateMixin):
    user_key          = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'sgkey')
    guestcategory_key = models.ForeignKey(GuestCategory, on_delete = models.CASCADE, blank = True, null = True, related_name = 'mkey')
    special_key       = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'specikey')
    house_key         = models.ForeignKey(HouseNo, on_delete = models.CASCADE, blank = True, null = True, related_name='gkey')
    guest_name        = models.CharField(max_length = 300)
    purpose           = models.TextField(blank = True, null = True)
    total_member      = models.IntegerField(blank = True, null = True)
    mobile_number     = models.IntegerField(blank = True, null = True)
    is_delete         = models.BooleanField(default = False)

    def __str__(self):
        return str(self.user_key)

    class Meta:
        ordering = ('-create_at',)
