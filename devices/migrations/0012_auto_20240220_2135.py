# Generated by Django 3.2.24 on 2024-02-20 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0011_alter_device_device_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_type',
        ),
        migrations.CreateModel(
            name='DeviceParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.parameter')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='parameters',
            field=models.ManyToManyField(through='devices.DeviceParameter', to='devices.Parameter'),
        ),
    ]
