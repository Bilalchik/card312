# Generated by Django 3.2.9 on 2023-08-23 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_remove_basicuser_card'),
        ('categories', '0002_auto_20230823_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/service/product')),
            ],
            options={
                'verbose_name': 'Фото для продукта',
                'verbose_name_plural': 'Фотки для продукта',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=223, verbose_name='Город')),
                ('description', models.TextField(verbose_name='Описание')),
                ('quantity', models.PositiveIntegerField(verbose_name='Кол-во')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.service_category', verbose_name='Категория')),
                ('characteristic', models.ManyToManyField(to='service.AdditionalInformation')),
                ('images', models.ManyToManyField(to='service.ProductImage', verbose_name='Фото')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.partners', verbose_name='Партнер')),
            ],
            options={
                'verbose_name': 'Товар/Услуга',
                'verbose_name_plural': 'Товары/Услуги',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=223, verbose_name='Название')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.service_category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Характеристика для Услуги',
                'verbose_name_plural': 'Характеристики для Услуги',
            },
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='characteristic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.characteristic'),
        ),
    ]