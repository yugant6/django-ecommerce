# Generated by Django 2.2 on 2020-04-30 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
    ]
