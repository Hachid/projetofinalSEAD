# Generated by Django 3.0.1 on 2019-12-20 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0005_auto_20191218_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gestaocontrato',
            old_name='contratada',
            new_name='Empresa',
        ),
    ]
