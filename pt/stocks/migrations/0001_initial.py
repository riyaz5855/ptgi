# Generated by Django 4.0.3 on 2022-04-15 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partycode', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=10)),
                ('color', models.IntegerField(max_length=3)),
                ('meter', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fabric', models.CharField(choices=[('lycra', 'Lycra'), ('cotton', 'Cotton'), ('rib', 'Rib')], max_length=10)),
            ],
        ),
    ]
