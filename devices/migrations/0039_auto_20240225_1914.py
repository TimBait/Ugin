# Generated by Django 3.2.24 on 2024-02-25 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0038_parametersettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='device_type',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='devices.devicetype'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ParameterSettings',
        ),
    ]
