# Generated by Django 3.2.24 on 2024-02-24 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0019_auto_20240224_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='parameters',
        ),
        migrations.AddField(
            model_name='parameter',
            name='device',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='devices.device'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='devices.devicemodel'),
            preserve_default=False,
        ),
    ]
