from django.shortcuts import render
from django.http import HttpResponse
from .models import Flan

# Create your views here.


def index(request):
    flans = Flan.objects.all()

    context = {"flans": flans}
    return render(request, "flan/index.html", context)


def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image_url = request.POST.get("image_url")
        shortName = request.POST.get("shortName")
        is_private = request.POST.get("is_private")
        if is_private == "on":
            is_private = True
        else:
            is_private = False
        flan = Flan(
            name=name,
            description=description,
            image_url=image_url,
            shortName=shortName,
            is_private=is_private,
        )
        flan.save()
        return render(request, "flan/index.html")
    return render(request, "flan/create.html")
