from typing import Any
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
  def _create_user(self, name, email, phone, password, **extra_fields):
    if not email:
      raise ValueError("You have not provided a valid e-mail address")
    
    email = self.normalize_email(email)
    user = self.model(email=email, name=name, phone=phone, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    
    return user
  
  def create_user(self, name=None, email=None, phone=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self.create_user(name, email, phone, password, **extra_fields)

  def create_superuser(self, name=None, email=None, phone=None, password=None, **extra_fields):
    # return super().create_superuser(name, email, phone, password, **extra_fields)
    
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self.create_user(name, email, phone, password, **extra_fields)


# Model for the user:
class User(AbstractBaseUser, PermissionsMixin):
  id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # default=uuid.uuid4().hex
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=255, blank=True, default='')
  phone = models.CharField(max_length=255, blank=True, default='')
  avatar = models.ImageField(upload_to='avatars', blank = True, null=True)
  
  is_active = models.BooleanField(default=True)
  is_superuser= models.BooleanField(default=False)
  is_staff= models.BooleanField(default=False)
  
  date_joined = models.DateTimeField(default=timezone.now)
  last_login = models.DateTimeField(blank=True, null=True)
  
  objects = CustomUserManager()
  
  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = []
  