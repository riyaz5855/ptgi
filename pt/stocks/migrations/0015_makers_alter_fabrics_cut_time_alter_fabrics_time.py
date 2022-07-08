# Generated by Django 4.0.3 on 2022-07-01 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0014_alter_fabrics_cut_time_alter_fabrics_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='fabrics',
            name='cut_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='fabrics',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 1, 23, 49, 46, 917636)),
        ),
    ]