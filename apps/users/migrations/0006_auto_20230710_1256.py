# Generated by Django 3.2.9 on 2023-07-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20230710_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Лайки', 'verbose_name_plural': 'Лайки'},
        ),
        migrations.AlterField(
            model_name='like',
            name='image',
            field=models.ImageField(blank=True, max_length=32, null=True, upload_to='apps/images/users', verbose_name='Фотография *(200x160)'),
        ),
        migrations.AlterField(
            model_name='like',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='like',
            name='title',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
