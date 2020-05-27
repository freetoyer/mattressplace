# Generated by Django 2.2.5 on 2019-12-04 19:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0011_auto_20191124_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_size',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.DeleteModel(
            name='Size_Price',
        ),
    ]