# Generated by Django 2.2.5 on 2019-11-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0007_auto_20191122_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='spring',
            field=models.BooleanField(default=True),
        ),
    ]