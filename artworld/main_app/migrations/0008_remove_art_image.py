# Generated by Django 2.2 on 2019-12-30 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20191228_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='image',
        ),
    ]
