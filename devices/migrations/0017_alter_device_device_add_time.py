# Generated by Django 3.2.24 on 2024-02-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0016_device_device_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_add_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
