from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm


def index(request):
    return render(request, 'customer/index.html')


def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            # Here you can add custom password handling or other logic
            customer.set_password(form.cleaned_data['password'])
            customer.save()
            # Redirect to login or other page after successful registration
            return redirect('login')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'customer/register.html', {'form': form})
