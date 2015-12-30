# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InsertaLogo', '0002_auto_20151228_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='time',
            new_name='fecha_registro',
        ),
    ]
