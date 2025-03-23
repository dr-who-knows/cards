from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

from .models import Card
from .forms import CardForm

def home(request):
    return render(request, 'flashcards/home.html')

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cards_list')
    else:
        form = CardForm()
    
    return render(request, 'flashcards/add_card.html', {'form': form})

def cards_list(request):
    cards = Card.objects.all()
    return render(request, 'flashcards/cards_list.html', {'cards': cards})

def tour_mode(request):
    cards = list(Card.objects.all())
    # Shuffle the cards for random order
    if cards:
        random.shuffle(cards)
    return render(request, 'flashcards/tour_mode.html', {'cards': cards})

def canvas_mode(request):
    cards = Card.objects.all()
    return render(request, 'flashcards/canvas_mode.html', {'cards': cards})

@csrf_exempt
def update_card_position(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        card_id = data.get('id')
        x_pos = data.get('x')
        y_pos = data.get('y')
        
        try:
            card = Card.objects.get(id=card_id)
            card.x_position = x_pos
            card.y_position = y_pos
            card.save()
            return JsonResponse({'status': 'success'})
        except Card.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Card not found'})
            
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
