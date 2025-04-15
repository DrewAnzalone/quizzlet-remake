from django.shortcuts import render

class Card:
    def __init__(self, hint, answer):
        self.hint = hint
        self.answer = answer

cards = [
    Card("What country are you in?", "United States"),
    Card("How many primary colors are there?", "3"),
    Card("What century is it?", "21st Century"),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def card_index(request):
    return render(request, 'cards/index.html', {"cards": cards})
