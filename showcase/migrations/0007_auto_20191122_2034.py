# Generated by Django 2.2.5 on 2019-11-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0006_auto_20191120_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_size',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_size',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
