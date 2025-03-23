from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_card, name='add_card'),
    path('list/', views.cards_list, name='cards_list'),
    path('tour/', views.tour_mode, name='tour_mode'),
    path('canvas/', views.canvas_mode, name='canvas_mode'),
    path('api/update-position/', views.update_card_position, name='update_card_position'),
] 