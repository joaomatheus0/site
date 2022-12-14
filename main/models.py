from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

class Account(AbstractUser):
    email = models.EmailField("E-mail", unique=True)
    password = models.CharField('Password', max_length=500, blank=False)
    nome = models.CharField('Nome', max_length=300, blank=False)
    telefone = models.CharField('Telefone', max_length=16, blank=False)
    is_trusty = models.BooleanField('trusty', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telefone']

    def __str__(self):
        return self.email
    
    objects = UsuarioManager()

class SocialAccount(models.Model):
    login = models.CharField('login', max_length=200, blank=False)
    password = models.CharField('Password', max_length=500, blank=False)
    social_network = models.CharField('Network', max_length=100, blank=False)
    account = models.ManyToManyField('Account', related_name='socialaccount')

    class Meta:
        ordering = ['social_network']

    def __str__(self):
        return self.login