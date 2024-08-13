from django.shortcuts import render


def custom_server_error(request):
    return render(request, '500.html', status=500)


def cookie_policy(request):
    return render(request, 'cookie_policy.html')
