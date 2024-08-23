from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import (
    CustomerRegistrationForm,
    CustomerLoginForm,
    CustomerProfileForm,
    CustomerPasswordChangeForm
)


def index(request):
    """
    Render the home page.
    """
    return render(request, 'customer/index.html')


def register(request):
    """
    Handle the registration of a new customer.

    If the request method is POST, process the registration form.
    On successful registration, redirect to the login page.
    Otherwise, render the registration form.
    """
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        # Instantiate a blank form
        form = CustomerRegistrationForm()
    return render(request, 'customer/register.html', {'form': form})


def login(request):
    """
    Handle the login of an existing customer.

    If the request method is POST, process the login form.
    On successful login, redirect to the index page.
    Otherwise, render the login form.
    """
    # Check if the user is already logged in
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomerLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        # Instantiate a blank form
        form = CustomerLoginForm()
    return render(request, 'customer/login.html', {'form': form})


@login_required
def profile(request):
    """
    Handle the customer's profile view and updates.

    If the request method is POST, process either the profile update
    or password change form based on the submitted data.
    On successful update, redirect back to the profile page.
    Otherwise, render the profile and password forms.
    """
    # Instantiate the forms with current user data
    profile_form = CustomerProfileForm(instance=request.user)
    password_form = CustomerPasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            profile_form = CustomerProfileForm(
                request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(
                    request, 'Your profile has been updated successfully.')
                return redirect('profile')
        elif 'change_password' in request.POST:
            password_form = CustomerPasswordChangeForm(
                request.user, request.POST)
            if password_form.is_valid():
                # Save the new password
                password_form.save()
                # Keep the user logged in
                update_session_auth_hash(request, password_form.user)
                messages.success(
                    request, 'Your password has been changed successfully.')
                return redirect('profile')

    # Render the profile page with both forms
    return render(request, 'customer/profile.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })


@login_required
def delete_account(request):
    """
    Handle the deletion of a customer's account.

    If the request method is POST, delete the user's account,
    log them out, and redirect to the home page.
    Otherwise, return a 403 Forbidden response.
    """
    if request.method == 'POST':
        user = request.user
        user.delete()
        # Log out the user and redirect to home page
        logout(request)
        return redirect('index')
    else:
        # Forbid GET requests
        return HttpResponseForbidden("You cannot access this page.")
