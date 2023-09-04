# Generated by Django 3.2.9 on 2023-08-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20230828_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Цена со скидкой'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Цена до скидки или акции'),
        ),
    ]