from django.shortcuts import render, redirect


def home(request):
    return render(request, 'base/home.html')


def sign_up(request):
    return render(request, 'base/sign_up.html')


def users(request):
    if request.user.is_staff:
        return render(request, 'base/users.html')
    elif request.user.is_authenticated:
        return redirect('base:home')
    return redirect('login')
