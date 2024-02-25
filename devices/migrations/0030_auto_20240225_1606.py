# Generated by Django 3.2.24 on 2024-02-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0029_auto_20240225_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='device_add_time',
        ),
        migrations.RemoveField(
            model_name='parameter',
            name='device',
        ),
        migrations.AddField(
            model_name='device',
            name='parameters',
            field=models.ManyToManyField(blank=True, to='devices.Parameter'),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='available_parameters',
            field=models.ManyToManyField(blank=True, to='devices.Parameter'),
        ),
    ]