# Generated by Django 2.2.5 on 2021-07-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0003_auto_20210713_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
        ),
    ]
