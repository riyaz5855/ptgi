# Generated by Django 4.0.3 on 2022-07-02 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0017_alter_fabrics_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabrics',
            name='cut_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='fabrics',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 2, 12, 29, 22, 68545)),
        ),
    ]
