from django.shortcuts import render


def index(request):
    return render(request, 'landingPage/index.html')