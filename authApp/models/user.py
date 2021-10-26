from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not email:
            raise ValueError('Users must have an username')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username=None
    id = models.BigAutoField(primary_key=True)
    password = models.CharField('Password', max_length = 256)
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    email = models.EmailField('Email', max_length = 100, unique=True)
    celular = models.CharField('Ceular', max_length=10)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'email' #describe el nombre del campo en el modelo de usuario que se usa como identificador único