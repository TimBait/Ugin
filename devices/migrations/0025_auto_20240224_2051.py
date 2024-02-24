# Generated by Django 3.2.24 on 2024-02-24 17:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0024_auto_20240224_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='serial_number',
        ),
        migrations.RemoveField(
            model_name='parameter',
            name='value',
        ),
        migrations.AddField(
            model_name='parameter',
            name='device_role',
            field=models.CharField(choices=[('KV', 'Квартальный'), ('SB_KL', 'Субкольцевой'), ('KL', 'Кольцевой'), ('VK', 'Вход в квартал'), ('P_VK', 'Идеальный ВК')], default='rk', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='ip_address',
            field=models.GenericIPAddressField(default='192.168.0.1', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='mac_address',
            field=models.CharField(default='00-1B-63-84-45-E6', max_length=17, unique=True, validators=[django.core.validators.RegexValidator(regex='^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='on_the_network',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='port_numbers',
            field=models.CharField(choices=[('8', '8'), ('12', '12'), ('24', '24'), ('48', '48')], default=24, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='serial_number',
            field=models.CharField(default=123456, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parameter',
            name='device',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='devices.device'),
        ),
        migrations.DeleteModel(
            name='ParameterField',
        ),
    ]
