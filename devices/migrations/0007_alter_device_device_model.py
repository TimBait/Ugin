# Generated by Django 3.2.24 on 2024-02-20 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_alter_device_device_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.devicemodel'),
        ),
    ]
