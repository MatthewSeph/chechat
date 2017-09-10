from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentication.forms import RegistrationForm

from ISW_2017 import settings


def index(request, template_name):
    if request.user.is_authenticated():
        return redirect(settings.HOME_URL)

    return render(request, template_name)


@login_required()
def home(request, template_name):
    return render(request, template_name)


def login_view(request, template_name):
    if request.user.is_authenticated():
        return redirect(settings.HOME_URL)

    if request.method == 'GET':
        return render(request, template_name)
    elif request.method == 'POST':
        return authenticate_user(request, template_name)


def authenticate_user(request, template_name):
    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(email=email, password=password)

    if user is not None:
        login(request, user)
        return redirect(settings.HOME_URL)

    else:
        return render(request, template_name, {'login_error': 'Le credenziali inserite non sono valide.'})


@login_required()
def logout_view(request):
    logout(request)
    return redirect(settings.INDEX_URL)


def sign_up(request, template_name):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect(settings.HOME_URL)
    else:
        form = RegistrationForm()
    return render(request, template_name, {'form': form})
