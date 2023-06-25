import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')
django.setup()

from newPage.models import Usuario

Usuario.objects.create_superuser(rut='admin', password='admin123', correo='admin@example.com')
