# Generated by Django 5.0.7 on 2024-07-14 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_cartitem_product_name_cartitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='delivery_time',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
    ]
