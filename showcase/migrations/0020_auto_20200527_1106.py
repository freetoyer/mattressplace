# Generated by Django 2.2.5 on 2020-05-27 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0019_auto_20200114_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cataloguefile',
            options={'verbose_name': 'Каталог', 'verbose_name_plural': 'Каталоги'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='short_title',
        ),
    ]