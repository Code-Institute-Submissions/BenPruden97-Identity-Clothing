# Generated by Django 3.2.9 on 2022-01-19 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_productreview_review_add_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='product',
            new_name='products',
        ),
    ]
