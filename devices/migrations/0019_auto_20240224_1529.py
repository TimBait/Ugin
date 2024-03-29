# Generated by Django 3.2.24 on 2024-02-24 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0018_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='parameters',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.parameter'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.devicemodel'),
        ),
    ]
