from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "index.html")


def co_details(request):
    return render(request, "co-details.html")


def services(request):
    return render(request, "services.html")


def products(request):
    return render(request, "products.html")


def mining(request):
    return render(request, "mining.html")


def contactUS(request):
    return render(request, "contactUS.html")


def productDetails(request):
    return render(request, "productDetails.html")


def storyDetail(request):
    return render(request, "story-details.html")
