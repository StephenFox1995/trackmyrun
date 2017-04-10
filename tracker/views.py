from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.urlresolvers import reverse
from django.forms import ValidationError
from . import forms


def register(request):
    if request.POST:
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            username = email

            try:
                user = get_user_model().objects.get(username=username)
                if user:
                    form.add_error(None, ValidationError("This user already exists."))
            except get_user_model().DoesNotExist:
                user = get_user_model().objects.create_user(username=username)

            user.set_password(password)
            user.email = email
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect(reverse('tracker:login'))

    else:
        form = forms.RegisterForm()
    return render(request, 'tracker/register.html', {'form': form})


def login_(request):
    if request.POST:
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('app:index'))
                else:
                    form.add_error(None, ValidationError(
                        "Your account is not active."
                    ))
            else:
                form.add_error(None, ValidationError(
                    "Incorrect email or password"
                ))
    else:
        form = forms.LoginForm()
    return render(request, 'tracker/login.html', {'form': form})
