# Generated by Django 4.1 on 2022-12-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_images/default.png', upload_to='post_images', verbose_name='Image'),
        ),
    ]
