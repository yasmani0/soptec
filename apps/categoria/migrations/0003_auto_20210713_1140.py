# Generated by Django 2.2.5 on 2021-07-13 16:40

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0002_categoria_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(default='ninguna', max_length=200),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='imagen'),
        ),
    ]
