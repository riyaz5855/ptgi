# Generated by Django 4.0.3 on 2022-07-04 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0022_alter_fabrics_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabrics',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 17, 42, 15, 40683)),
        ),
    ]
