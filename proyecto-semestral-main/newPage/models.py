from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True, db_column='idTipo', verbose_name='ID_tipo_Usuario', default=0)
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipoUsuario)



class UsuarioManager(BaseUserManager):
    def create_user(self, rut, password=None, **extra_fields):
        if not rut:
            raise ValueError("The 'rut' field must be set")
        
        user = self.model(rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(rut, password, **extra_fields)

    def get_by_natural_key(self, rut):
        return self.get(rut=rut)


class Usuario(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    appPaterno = models.CharField(max_length=30, blank=False, null=False)
    appMaterno = models.CharField(max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=True, null=True)
    tipoUsuario = models.ForeignKey('tipoUsuario', on_delete=models.CASCADE, db_column='idTipo', null=True)
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    activo = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=13, blank=False, null=False)
    is_staff = models.BooleanField(default=False)  # Add is_staff field
    is_superuser = models.BooleanField(default=False)  # Add is_superuser field
    

    USERNAME_FIELD = 'rut'

    objects = UsuarioManager()


    def __str__(self):
        return self.rut
