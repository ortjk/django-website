# Generated by Django 4.1 on 2022-12-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images', verbose_name='Image'),
        ),
    ]
