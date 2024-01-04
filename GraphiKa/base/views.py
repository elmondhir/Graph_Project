from django.shortcuts import render, redirect
from .models import Country
# Create your views here.


rooms = [
    {'id':1, "name": "This is room 1"},
    {'id':2, "name": "This is room 2"},
    {'id':3, "name": "This is room 3"},
]


def home(request):
    context = {'rooms':rooms}
    return render(request, "base/home.html", context=context)
    # return HttpResponse("Home page")


def room(request, pk):
    return render(request, "base/room.html")
    # return HttpResponse("Room page")

def create_country(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('label')
        new_country = Country(code=code, name=name)
        new_country.save()
        return redirect('country_list')

    return render(request, 'base/create_country.html')

def country_list(request):
    countries = Country.nodes.all()
    return render(request, 'base/country_list.html', {'countries': countries})