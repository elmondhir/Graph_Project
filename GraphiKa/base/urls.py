from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path('network-graph/', views.network_graph_view, name='network_graph_view'),
    path('countries/', views.country_list, name='country_list'),
    path('countries/create/', views.create_country, name='create_country'),

]
