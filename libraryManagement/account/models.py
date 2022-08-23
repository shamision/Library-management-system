from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.model(
            username = username,
            password = password,
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.staff = True
        user.superuser = True
        user.is_active = True
        user.user_type = user.USER_TYPE[1][1]
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    USER_TYPE = [
        ['U','Student'],
        ['S','Librarian']
    ]
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(unique=True, max_length=100)
    user_type = models.CharField(choices=USER_TYPE, max_length=100)
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects= UserManager()
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def get_name(self):
        return self.username
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.superuser