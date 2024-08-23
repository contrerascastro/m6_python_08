from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    images = [
        {
            "img": "static/img/img1.jpg",
            'message' : 'El mejor postre de chocolate que puedes probar'},
        
        {
            "img": "static/img/img2.jpg",
            'message' : 'El mejor postre de chocolate que puedes probar'},

        {
            "img": "static/img/img3.jpg",
            'message' : 'El mejor postre de chocolate que puedes probar'},
    ]
    context = {"images": images}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def welcome(request):
    return render(request, "welcome.html")
