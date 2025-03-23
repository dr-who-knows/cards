from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
import random

from .models import Card, UserProfile
from .forms import CardForm, CustomUserCreationForm, CustomAuthenticationForm

def home(request):
    return render(request, 'flashcards/home.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'flashcards/register.html', {'form': form})
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
        
    return render(request, 'flashcards/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')
    
@login_required
def profile_view(request):
    # Get card count for the user stats
    card_count = Card.objects.filter(user=request.user).count()
    
    context = {
        'card_count': card_count
    }
    
    return render(request, 'flashcards/profile.html', context)

@login_required
def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            # Save the form but don't commit to the database yet
            card = form.save(commit=False)
            # Set the user to the current user
            card.user = request.user
            # Now save to the database
            card.save()
            return redirect('cards_list')
    else:
        form = CardForm()
    
    return render(request, 'flashcards/add_card.html', {'form': form})

@login_required
def cards_list(request):
    cards = Card.objects.filter(user=request.user)
    return render(request, 'flashcards/cards_list.html', {'cards': cards})

@login_required
def tour_mode(request):
    cards = list(Card.objects.filter(user=request.user))
    # Shuffle the cards for random order
    if cards:
        random.shuffle(cards)
    return render(request, 'flashcards/tour_mode.html', {'cards': cards})

@login_required
def canvas_mode(request):
    cards = Card.objects.filter(user=request.user)
    canvas_position = {}
    
    # If user is authenticated, get their canvas position settings
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            canvas_position = {
                'translate_x': profile.canvas_translate_x,
                'translate_y': profile.canvas_translate_y,
                'scale': profile.canvas_scale
            }
        except UserProfile.DoesNotExist:
            # Create profile if it doesn't exist
            profile = UserProfile.objects.create(user=request.user)
            
    return render(request, 'flashcards/canvas_mode.html', {
        'cards': cards,
        'canvas_position': canvas_position
    })

@csrf_exempt
@login_required
def update_card_position(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_id = data.get('id')
        x_pos = data.get('x')
        y_pos = data.get('y')
        
        try:
            # Only allow updating cards that belong to the current user
            card = Card.objects.get(id=card_id, user=request.user)
            card.x_position = x_pos
            card.y_position = y_pos
            card.save()
            return JsonResponse({'status': 'success'})
        except Card.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Card not found or not authorized'})
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
@csrf_exempt
@login_required
def update_canvas_position(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'User not authenticated'})
            
        data = json.loads(request.body)
        translate_x = data.get('translate_x')
        translate_y = data.get('translate_y')
        scale = data.get('scale')
        
        try:
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            profile.canvas_translate_x = translate_x
            profile.canvas_translate_y = translate_y
            profile.canvas_scale = scale
            profile.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
