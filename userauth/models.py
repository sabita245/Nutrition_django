from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import UserManager
from django.db.models.signals import pre_save

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(verbose_name='email',max_length=255,unique=True,null=True,blank=True)
    name=models.CharField(max_length=100,verbose_name='name',null=True,blank=True)
    age=models.PositiveBigIntegerField(default=5,verbose_name='age')
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    objects=UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['name','age']

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #   "Does the user have a specific permission?"
    #   # Simplest possible answer: Yes, always
    #   return self.is_admin

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin



