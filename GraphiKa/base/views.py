from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "home.html")
    # return HttpResponse("Home page")


def room(request):
    return render(request, "room.html")
    # return HttpResponse("Room page")