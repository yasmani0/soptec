# Generated by Django 2.2.5 on 2021-07-13 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0010_auto_20210606_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='imagen',
        ),
    ]