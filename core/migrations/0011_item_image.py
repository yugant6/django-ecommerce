# Generated by Django 2.2 on 2020-04-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200430_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/12.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
