# Generated by Django 3.2.9 on 2023-08-22 05:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230821_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата регистрации'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partners',
            name='activity_type',
            field=models.CharField(default=1, max_length=64, verbose_name='Тип деятельности'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partners',
            name='inn',
            field=models.CharField(default=1, max_length=16, verbose_name='ИНН'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partners',
            name='org',
            field=models.CharField(default=1, max_length=64, verbose_name='Организационная правовая форма'),
            preserve_default=False,
        ),
    ]
