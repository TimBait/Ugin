# Generated by Django 3.2.24 on 2024-02-20 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0012_auto_20240220_2135'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='deviceparameter',
            unique_together={('device', 'parameter')},
        ),
    ]
