# Generated by Django 3.2.4 on 2021-10-01 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='categories',
            name='category_image',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='avi',
            field=models.CharField(default='https://www.kindpng.com/imgv/obiRob_user-avatar-png-user-avatar-icon-png-transparent/', max_length=400),
        ),
        migrations.AddField(
            model_name='profile',
            name='proffession',
            field=models.CharField(blank=True, default='Writter', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]