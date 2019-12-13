# Generated by Django 2.2.5 on 2019-12-13 17:39

from django.db import migrations, models
import showcase.models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0015_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.ImageField(upload_to=showcase.models.image_folder),
        ),
    ]
