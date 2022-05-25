#como ya vamos a administrar todos los usuarios y hasta los super-usuarios
#Django nos pide managers para poder administrarlos o re-definirlos
#es por eso que se crea este archivo

from django.db import models
#
from django.contrib.auth.models import BaseUserManager

#como ahora depende de nosotros la creacion y gestion de usuarios, es necesario
#crear una funcion que permite crear los super usuarios y los usuarios
#primero crearemos la funcion de los superusuarios y por eso necesitamos
#definir si el usuarios puede loguearse al admin (is_staff) ó
#si el usuario es superusuario (is_superuser)
class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self, username, email, password, is_staff, is_superuser, is_active,**extra_fields):
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
            #por qué hay campos como "username=username", porque como "user" es una instancia del...
            #modelo entonces el valor de campo username es igual al parametro recibido en la...
            #funcion con el nombre username


            #no es necesario que is_staff e is_superuser esten definidos en el modelo...
            #porque ya se heredan de la clase AbstractBaseUser

            #**extra_fields son campos adicionales que se pueden solicitar si es necesario al...
            #momento de crear un superusuario, los campos adicionales que se pueden soliciar...
            #son los demas campos que estan en el modelo que aca no estan definidos
        )

        #esta linea lo que hace es hashear el password para no dejarlo a la vista...
        #de todos
        user.set_password(password)

        user.save(using=self.db) #"using=self.db" hace referencia a que la informacion...
        #se guardará en la BD que estamos usando
        return user


    def create_user(self, username, email,password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,False,**extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, True,**extra_fields)
        #como _create_user recibe...
        #estos parametros (self, username, email, password, is_staff, is_superuser, **extra_fields)...
        #e is_staff, is_superuser, son campos booleanos, es por eso que al momento de retornarlos...
        #se retorna True, True indicando que is_staff=True e is_superuser=True

        #con el _create_user defino que la funcion es privada y solo se puede...
        #acceder desde este archivo y no desde otro

    def cod_validation(self, id_user, cod_registro):
        if self.filter(id=id_user, codregistro=cod_registro).exists():
            return True
        else:
            return False