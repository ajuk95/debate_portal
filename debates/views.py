from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserRole
from .forms import RegistrationForm
from .models import Debate
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration (optional)
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'debates/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use your custom user model for authentication
        user = UserRole.objects.get(username=username)

        # Check the password
        if user.check_password(password):
            # Authenticate the user
            login(request, user)
            return redirect('debate_list')
    return render(request, 'debates/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def debate_list(request):
    debates = Debate.objects.filter(is_open=True)
    return render(request, 'debates/debate_list.html', {'debates': debates})


def user_profile(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    return render(request, 'debates/user_profile.html', {'user_profile': user_profile})
