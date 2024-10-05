from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, name, department, mathno, password=None):
        if not mathno:
            raise ValueError("Users must have a Math Number (MathNo)")
        if not name:
            raise ValueError("Users must have a name")
        if not department:
            raise ValueError("Users must have a department")

        # Create and normalize the user
        user = self.model(
            name=name,
            department=department,
            mathno=mathno
        )
        # Set the password using Django's set_password method to hash it
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, department, mathno, password=None):
        user = self.create_user(
            name=name,
            department=department,
            mathno=mathno,
            password=password
        )
        # Set admin permissions
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user