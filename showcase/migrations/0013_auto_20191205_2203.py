# Generated by Django 2.2.5 on 2019-12-05 19:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0012_auto_20191204_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='full_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
