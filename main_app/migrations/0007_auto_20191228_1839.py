# Generated by Django 2.2 on 2019-12-28 18:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_auto_20191228_0045'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItem',
            new_name='Cart',
        ),
        migrations.AlterField(
            model_name='art',
            name='price',
            field=models.FloatField(),
        ),
    ]
