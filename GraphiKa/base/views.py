from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "base/home.html")
    # return HttpResponse("Home page")


def room(request, pk):
    return render(request, "base/room.html")
    # return HttpResponse("Room page")