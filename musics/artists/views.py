from django.shortcuts import render


def artist(request, id):
    return render(request, 'artists/details.html')
