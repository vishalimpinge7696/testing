from django.db import models
# from __future__ import unicode_literals
from django.contrib.auth.models import User
# Create your models here.


class Signup(models.Model):
    name = models.CharField(max_length=150)
    photo = models.FileField(upload_to='images/', null=True, blank=True, help_text="Upload only .png, .jpg & .jpeg image extension.")
    email = models.EmailField(max_length=150)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    contact = models.IntegerField()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "signups"
        verbose_name = "SIGNUP"
        managed = True

