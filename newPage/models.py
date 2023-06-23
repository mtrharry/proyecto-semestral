from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(
        primary_key=True, db_column='idTipo', verbose_name='ID_tipo_Usuario')
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipoUsuario)


class UsuarioManager(BaseUserManager):
    def create_user(self, rut, nombre, appPaterno, appMaterno, fechaNacimiento, tipoUsuario, correo, telefono, password=None):
        # Create a new user object
        user = self.model(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            fechaNacimiento=fechaNacimiento,
            tipoUsuario=tipoUsuario,
            correo=correo,
            telefono=telefono,
            activo=1,
        )

        # Set the user's password
        user.set_password(password)
        
        # Save the user object
        user.save(using=self._db)
        return user

    # Define a method for creating superusers (if needed)
    def create_superuser(self, rut, nombre, appPaterno, appMaterno, fechaNacimiento, tipoUsuario, correo, telefono, password=None):
        user = self.create_user(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            fechaNacimiento=fechaNacimiento,
            tipoUsuario=tipoUsuario,
            correo=correo,
            telefono=telefono,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    appPaterno = models.CharField(max_length=30, blank=False, null=False)
    appMaterno = models.CharField(max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    tipoUsuario = models.ForeignKey('tipoUsuario', on_delete=models.CASCADE, db_column='idTipo')
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    activo = models.IntegerField()
    direccion = models.CharField(max_length=100, blank=True, null=True)


    # Add the custom manager
    objects = UsuarioManager()

    # Set the username field to 'rut'
    USERNAME_FIELD = 'rut'