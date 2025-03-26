from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic import ListView


from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PortfolioEntryForm, UserLoginForm
from .models import PortfolioEntry, User, Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Учетная запись, созданная для {username}! Теперь вы можете войти в систему.')
            print(username)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
        messages.error(request, "Неверный логин или пароль!")

    return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваша учетная запись была обновлена!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profiles': profiles
    })


@login_required
def portfolio(request):
    portfolios = PortfolioEntry.objects.all()
    if request.method == 'POST':
        form = PortfolioEntryForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_entry = form.save(commit=False)
            portfolio_entry.user = request.user
            portfolio_entry.save()
            messages.success(request, f'Добавлена запись в портфолио!')
            return redirect('portfolio_detail')
    else:
        form = PortfolioEntryForm()

    entries = PortfolioEntry.objects.filter(user=request.user).order_by('-published_date')
    return render(request, 'portfolio.html', {'form': form, 'entries': entries, 'portfolios': portfolios})



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def portfolio_detail(request):
    entries = PortfolioEntry.objects.filter(user=request.user).order_by('-published_date')
    return render(request, 'portfolio_detail.html', {'entries': entries})
