from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')
    bio = models.TextField(max_length=500, blank=True, verbose_name='о себе')
    location = models.CharField(max_length=100, blank=True, verbose_name='местоположение')
    birth_date = models.DateField(null=True, blank=True, verbose_name='дата рождения')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.user} Profile'

class PortfolioEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name='фото')
    published_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='дата публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
