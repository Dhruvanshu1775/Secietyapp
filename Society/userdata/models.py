from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TimeDateMixin(models.Model):
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)


class UserInfo(TimeDateMixin):
    user_key     = models.OneToOneField(User, on_delete = models.CASCADE)
    is_secretary = models.BooleanField(default = False)
    is_member    = models.BooleanField(default = False)
    is_security  = models.BooleanField(default = False)

    def __str__(self):
        return str(self.user_key)
