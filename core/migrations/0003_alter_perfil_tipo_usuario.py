# Generated by Django 5.0.9 on 2024-11-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_boleta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo_usuario',
            field=models.CharField(choices=[('Cliente', 'Cliente'), ('Administrador', 'Administrador'), ('Medico', 'Medico'), ('Secretario', 'Secretario'), ('Cajero', 'Cajero'), ('Superusuario', 'Superusuario')], max_length=50, verbose_name='Tipo de usuario'),
        ),
    ]
