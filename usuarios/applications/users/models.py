from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

#PermissionsMixin le dice a Django que cuando utilice algo acerca del modelo user
#utilizará exclusivamente este modelo creado y no el modelo propio de user
#que trae internamente Django
class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
        ('O','Otros'),
    )

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    codregistro = models.CharField(max_length=6, blank=True)
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username' #con esto le digo a Django con cual de los atributos
    #anteriores va a ser el campo con el que me voy a loguear

    REQUIRED_FIELDS = ['email'] #campos adicionales necesarios para loguearme

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos