from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.forms import ValidationError
from . import forms


def register(request):
    form = forms.RegisterForm(request.POST)
    if request.POST:
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
    return render(request, 'tracker/register.html', {'form': form})
