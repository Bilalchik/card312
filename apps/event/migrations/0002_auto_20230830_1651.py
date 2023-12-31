# Generated by Django 3.2.9 on 2023-08-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Стоимость до'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Стоимость от'),
        ),
    ]
