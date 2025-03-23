from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('add/', views.add_card, name='add_card'),
    path('list/', views.cards_list, name='cards_list'),
    path('tour/', views.tour_mode, name='tour_mode'),
    path('canvas/', views.canvas_mode, name='canvas_mode'),
    path('api/update-position/', views.update_card_position, name='update_card_position'),
    path('api/update-canvas-position/', views.update_canvas_position, name='update_canvas_position'),
] 