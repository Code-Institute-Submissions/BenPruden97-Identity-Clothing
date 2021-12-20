# Generated by Django 3.2.9 on 2021-12-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.CharField(choices=[('XXSmall', 'XXS'), ('XSmall', 'XS'), ('Small', 'S'), ('Medium', 'M'), ('Large', 'L'), ('XLarge', 'XL'), ('XXLarge', 'XXL')], max_length=7),
        ),
    ]
