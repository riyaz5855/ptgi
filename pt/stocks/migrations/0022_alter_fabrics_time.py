# Generated by Django 4.0.3 on 2022-07-04 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0021_alter_fabrics_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabrics',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 17, 39, 7, 569491)),
        ),
    ]