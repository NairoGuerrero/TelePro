from django.shortcuts import render


def index(request):
    return render(request, 'landingPage/index.html')


def about(request):
    return render(request, 'landingPage/about.html')


def services(request):
    return render(request, 'landingPage/services.html')


def features(request):
    return render(request, 'landingPage/features.html')


def faq(request):
    return render(request, 'landingPage/faq.html')


def contact(request):
    return render(request, 'landingPage/contact.html')


def privacy(request):
    return render(request, 'landingPage/privacy.html')


def sitemap_view(request):
    return render(request, 'landingPage/sitemap.html')