# Generated by Django 4.0.3 on 2022-06-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_alter_fabrics_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabrics',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
