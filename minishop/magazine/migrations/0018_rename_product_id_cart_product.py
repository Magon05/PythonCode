# Generated by Django 5.0.4 on 2024-09-28 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0017_rename_product_cart_product_id_cart_product_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product_id',
            new_name='product',
        ),
    ]
