# Generated by Django 3.2.9 on 2023-02-22 10:14

import apps.categories.services
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.categories.services.get_upload_path)),
                ('icon', models.FileField(blank=True, null=True, upload_to=apps.categories.services.get_upload_path, validators=[apps.categories.services.validate_file_extension])),
                ('is_main', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='categories.category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
            },
        ),
    ]
