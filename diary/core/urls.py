from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password_reset', auth_views.LoginView.as_view(template_name='login.html'), name='password_reset'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/detail', views.portfolio_detail, name='portfolio_detail'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)