# Generated by Django 5.0.6 on 2024-06-25 21:53

import publico.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto_perfil',
            field=models.ImageField(null=True, upload_to='cliente_fotos_perfil'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=publico.models.GeneroCliente.choices, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='tipo',
            field=models.CharField(choices=[('EMAIL', 'E-mail'), ('CELULAR', 'Celular'), ('INSTAGRAM', 'Instagram')], max_length=100),
        ),
    ]
