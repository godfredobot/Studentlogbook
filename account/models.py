from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from account.managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    mat_no = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Manager for the User model
    objects = CustomUserManager()

    USERNAME_FIELD = 'mat_no'  # Login with mathno instead of username
    REQUIRED_FIELDS = ['name', 'department']  # Fields required in addition to the mathno

    def __str__(self):
        return f"{self.name} ({self.mathno})"

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app 'app_label'?"""
        return True
    
class StudentLog(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    date = models.DateTimeField(default=timezone.now)
    entry = models.TextField()

    def __str__(self):
        return f"Log for {self.student.mat_no} on {self.date}"