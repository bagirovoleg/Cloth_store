from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib import auth, messages
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created.')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your personal data has been changed')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Store - Profile',
        'form': form
               }
    return render(request, 'users/profile.html', context)
