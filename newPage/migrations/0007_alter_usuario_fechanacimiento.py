# Generated by Django 4.2.1 on 2023-06-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newPage', '0006_usuario_groups_usuario_is_staff_usuario_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fechaNacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]