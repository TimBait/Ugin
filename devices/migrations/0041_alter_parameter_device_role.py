# Generated by Django 3.2.24 on 2024-02-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0040_auto_20240225_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='device_role',
            field=models.CharField(blank=True, choices=[('Квартальный', 'Квартальный'), ('Субкольцевой', 'Субкольцевой'), ('Кольцевой', 'Кольцевой'), ('Вход в квартал', 'Вход в квартал'), ('Идеальный ВК', 'Идеальный ВК')], max_length=20, null=True, verbose_name='Device role'),
        ),
    ]
