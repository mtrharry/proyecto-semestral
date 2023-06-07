from django.contrib import admin
# Register your models here.
from .models import tipoUsuario, Usuario

admin.site.register(tipoUsuario)
admin.site.register(Usuario) 
