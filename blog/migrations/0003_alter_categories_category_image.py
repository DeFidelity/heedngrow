# Generated by Django 3.2.10 on 2022-02-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220224_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_image',
            field=models.ImageField(null=True, upload_to='media/category/'),
        ),
    ]