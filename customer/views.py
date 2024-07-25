from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import CustomerRegistrationForm, CustomerLoginForm


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
