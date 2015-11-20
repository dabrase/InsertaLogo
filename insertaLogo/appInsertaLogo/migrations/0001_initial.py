# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=80)),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.TextField(help_text=b'Direccion de correo Electronico', verbose_name=b'Email')),
            ],
        ),
    ]