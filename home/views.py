from django.shortcuts import render

# Create your views here.
# zaid zaid1234
# tausif zumrahMarry123


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')
