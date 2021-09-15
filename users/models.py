from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, name, lname, password=None, **other_fields):
        if not email:
            raise ValueError("Email es requerido")
        if not username:
            raise ValueError("Nombre de Usuario es requerido")
        if not name:
            raise ValueError("Nombre es requerido")
        if not lname:
            raise ValueError("Apellido Paterno es requerido")

        email = self.normalize_email(email)

        user = self.model(email=email, username=username, name=name, lname=lname, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, name, lname, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        
        superuser = self.create_user(email, username, name, lname, password, **other_fields)
        superuser.save()
        return superuser


class User(AbstractBaseUser):
    
    email = models.EmailField("Email", max_length=40, unique=True)
    username = models.CharField("Nombre de Usuario", max_length=20, unique=True)
    name = models.CharField("Nombre", max_length=20)
    name2 = models.CharField("Segundo Nombre", max_length=20, blank=True)
    lname = models.CharField("Apellido Paterno", max_length=20)
    lname2 = models.CharField("Apellido Materno", max_length=20, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name", "lname"]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
