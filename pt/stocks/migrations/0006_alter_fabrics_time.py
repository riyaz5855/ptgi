# Generated by Django 4.0.3 on 2022-06-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_fabrics_time_alter_fabrics_maker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabrics',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
