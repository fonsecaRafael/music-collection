from django.shortcuts import render, redirect

from musics.base.models import User


def home(request):
    return render(request, 'base/home.html')


def sign_up(request):
    return render(request, 'base/sign_up.html')


def only_admin_should_pass(request):
    if request.user.is_authenticated and request.user.is_staff:
        return True
    return False


def users(request):
    if only_admin_should_pass(request):
        users = User.objects.exclude(id=request.user.id)
        return render(request, 'base/users.html', context={'users': users})
    return redirect('base:home')


def upgrade(request, id):
    if only_admin_should_pass(request):
        user = User.objects.get(id=id)
        user.is_staff = True
        user.save()
        return redirect('base:users')
    return redirect('base:home')



def downgrade(request, user_id):
    return render(request, 'base/sign_up.html')
