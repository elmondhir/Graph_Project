from django.shortcuts import render, redirect
from .models import Country, Room
# Create your views here.
import json
import os
# rooms = [
#     {'id':1, "name": "This is room 1"},
#     {'id':2, "name": "This is room 2"},
#     {'id':3, "name": "This is room 3"},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, "base/home.html", context=context)
    # return HttpResponse("Home page")


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, "base/room.html", context=context)
    # return HttpResponse("Room page")

def network_graph_view(request):
    # Your network data processing logic here
    # Example data with more nodes and links:
    nodes = [
        {
      "caption": "Screen Actors Guild Award for Outstanding Performance by a Female Actor in a Miniseries or Television Movie",
      "type": "award",
      "id": 595472
    },
    {
      "caption": "Children of the Corn III: Urban Harvest",
      "type": "movie",
      "id": 626470
    }
    ]
    edges = [
    {
      "source": 595472,
      "target": 626470,
      "caption": "ACTED_IN"
    }
    ]

    # Convert data to JSON
    graph_data = {'nodes': nodes, 'edges': edges}
    graph_json = json.dumps(graph_data)

    # Save the JSON data to a file
    with open('base/templates/base/data.json', 'w') as file:
        file.write(graph_json)

    return render(request, 'base/network.html', {'graph_json': graph_json})


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