from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def sign_up(request):
    return render(request, 'base/sign_up.html')
