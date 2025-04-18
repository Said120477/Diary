# Generated by Django 4.2.20 on 2025-03-26 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_portfolioentry_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioentry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='portfolioentry',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='portfolioentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='portfolioentry',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='portfolioentry',
            name='title',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='portfolioentry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
