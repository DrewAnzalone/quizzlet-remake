from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Card

def find_index(arr, call):
    for idx, obj in enumerate(arr):
        if call(obj):
            return idx
    return -1

class CardCreate(CreateView):
    model = Card
    fields = '__all__'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def card_index(request):
    cards = Card.objects.order_by('id')
    return render(request, 'cards/index.html', {"cards": cards})

def card_view(request, card_id):
    neighbors = [None, None]
    cards = Card.objects.order_by('id')
    idx = find_index(cards, lambda x: x.id == card_id)

    # TODO fix assuming valid id
    if idx == 0 and len(cards) > 1:
        neighbors[1] = cards[1].id
    elif idx == len(cards)-1 and len(cards) > 1:
        neighbors[0] = cards[idx-1].id
    elif len(cards) > 2:
        neighbors = [cards[idx-1].id, cards[idx+1].id]
    
    return render(request, 'cards/detail.html', {'card': cards[idx], 'prev': neighbors[0], 'next': neighbors[1]})
