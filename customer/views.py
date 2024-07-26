from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from .forms import (
    CustomerRegistrationForm,
    CustomerLoginForm,
    CustomerProfileForm,
    CustomerPasswordChangeForm
)


def index(request):
    return render(request, 'customer/index.html')


def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customer/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomerLoginForm()
    return render(request, 'customer/login.html', {'form': form})


@login_required
def profile(request):
    # Instantiate the forms outside the POST check so they are always available
    profile_form = CustomerProfileForm(instance=request.user)
    password_form = CustomerPasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            profile_form = CustomerProfileForm(
                request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile')
        elif 'change_password' in request.POST:
            password_form = CustomerPasswordChangeForm(
                request.user, request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)
                return redirect('profile')

    return render(request, 'customer/profile.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        # Log out the user and redirect to home page
        logout(request)
        return redirect('index')
    else:
        return HttpResponseForbidden("You cannot access this page.")
