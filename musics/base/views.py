from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from musics.base.forms import UserForm
from musics.base.models import User


@require_http_methods(["GET"])
def home(request):
    return render(request, 'base/home.html')


@require_http_methods(["GET", "POST"])
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


@login_required()
@require_http_methods(["GET"])
def users(request):
    if only_admin_should_pass(request):
        users = User.objects.exclude(id=request.user.id)
        return render(request, 'base/users.html', context={'users': users})
    return redirect('base:home')


@login_required()
@require_http_methods(["POST"])
def upgrade(request):
    if only_admin_should_pass(request):
        user = User.objects.get(id=request.POST['id_user_up'])
        user.is_staff = True
        user.save()
        return redirect('base:users')
    return redirect('base:home')


@login_required()
@require_http_methods(["POST"])
def downgrade(request):
    if only_admin_should_pass(request):
        user = User.objects.get(id=request.POST['id_user_del'])
        user.is_staff = False
        user.save()
        return redirect('base:users')
    return redirect('base:home')
