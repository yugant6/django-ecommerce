# Generated by Django 2.2 on 2020-04-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/templates/shirt.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
