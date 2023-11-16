from django.shortcuts import render, redirect

from musics.base.forms import UserForm
from musics.base.models import User


def home(request):
    return render(request, 'base/home.html')


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                full_name=form.cleaned_data['full_name'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            user.save()
            return redirect('login')

    form = UserForm()
    return render(request, 'base/sign_up.html', {'form': form})


def only_admin_should_pass(request):
    if request.user.is_authenticated and request.user.is_staff:
        return True
    return False


def users(request):
    if only_admin_should_pass(request):
        users = User.objects.exclude(id=request.user.id)
        return render(request, 'base/users.html', context={'users': users})
    return redirect('base:home')


def upgrade(request, user_id):
    if only_admin_should_pass(request):
        user = User.objects.get(id=user_id)
        user.is_staff = True
        user.save()
        return redirect('base:users')
    return redirect('base:home')


def downgrade(request, user_id):
    if only_admin_should_pass(request):
        user = User.objects.get(id=user_id)
        user.is_staff = False
        user.save()
        return redirect('base:users')
    return redirect('base:home')
