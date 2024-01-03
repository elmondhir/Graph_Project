from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path('countries/', views.country_list, name='country_list'),
    path('countries/create/', views.create_country, name='create_country'),

]
