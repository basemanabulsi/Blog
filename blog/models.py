# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db import models

class Article(models.Model):
    """Articles table """
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff=True,
            is_admin=True
        )
        return user



class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True) # Can login
    staff = models.BooleanField(default=False) # Staff user non superuser
    admin = models.BooleanField(default=False) # superuser

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email 

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
        
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
