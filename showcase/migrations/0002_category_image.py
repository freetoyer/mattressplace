# Generated by Django 2.2.5 on 2019-11-17 18:10

from django.db import migrations, models
import showcase.models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to=showcase.models.image_folder),
            preserve_default=False,
        ),
    ]