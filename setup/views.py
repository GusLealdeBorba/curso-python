from django.shortcuts import render


def home_setup(request):
    return render(request, 'home_setup.html')