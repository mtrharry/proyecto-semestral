# Generated by Django 4.2.1 on 2023-06-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newPage', '0007_alter_usuario_fechanacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='activo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]