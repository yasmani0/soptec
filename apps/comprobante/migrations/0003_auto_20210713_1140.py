# Generated by Django 2.2.5 on 2021-07-13 16:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comprobante', '0002_auto_20210606_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='imagen'),
        ),
    ]