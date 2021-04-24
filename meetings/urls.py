from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.show_rooms, name="rooms"),
    path('new', views.nouveau, name="nouveau"),
]