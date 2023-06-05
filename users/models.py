from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.create(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Адміністратор повинен мати поле is_superuser=True.')
        return self.create_user(email, password=password, **extra_fields)


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    STATUS_CHOICES = (
        (False, 'Offline'),
        (True, 'Online'),
    )

    username = None
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True, verbose_name='Стать')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата народження')
    status = models.BooleanField(choices=STATUS_CHOICES, default=False, verbose_name='Статус')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Administrator(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Адміністратор'
        verbose_name_plural = 'Адміністратори'


class Client(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'
