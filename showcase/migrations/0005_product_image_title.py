# Generated by Django 2.2.5 on 2019-11-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0004_product_image_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_image',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
