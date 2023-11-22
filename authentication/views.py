from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from . import forms


def login_page(request):
    formLogin = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        formLogin = forms.LoginForm(request.POST)
        if formLogin.is_valid():
            user = authenticate(
                username=formLogin.cleaned_data['username'],
                password=formLogin.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides'

    return render(request, 'authentication/login.html',
                  context={'form': formLogin, 'message': message})


def signup_page(request):
    form = forms.SignupForm(request.POST)
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html',
                  context={'form': form})


def logout_page(request):

    logout(request)
    return redirect('login')
