import uuid
from datetime import datetime

from django.db import models


# Create your models here.

class User(models.Model):
    GENDERS = (("MALE", "MALE"),
               ("FEMALE", "FEMALE"),
               ("OTHER", "OTHER"))
    username = models.CharField(max_length=254, primary_key=True)
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=20, null=True)
    dob = models.DateTimeField(null=True)
    password = models.CharField(max_length=256)
    gender = models.CharField(max_length=124, choices=GENDERS, default=None)
    profile_pic = models.CharField(max_length=512)
    created_on = models.DateTimeField(default=datetime.now())


class LoginEntry(models.Model):
    user = models.ForeignKey(User)
    login_time = models.DateTimeField(default=datetime.now())
    client_id = models.CharField(max_length=256)
    auth_token = models.CharField(max_length=512, default=str(uuid.uuid4()))
    is_active = models.BooleanField(default=True)
