# Generated by Django 4.2.20 on 2025-03-25 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioentry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='portfolioentry',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, verbose_name='о себе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100, verbose_name='местоположение'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
