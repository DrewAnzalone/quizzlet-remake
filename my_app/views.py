from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Card

def find_index(arr, call):
    for idx, obj in enumerate(arr):
        if call(obj):
            return idx
    return -1

class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['hint', 'answer']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['hint', 'answer']

class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def card_index(request):
    cards = Card.objects.filter(user=request.user).order_by('id')
    return render(request, 'cards/index.html', {"cards": cards})

@login_required
def card_detail(request, card_id):
    neighbors = [None, None]
    cards = Card.objects.order_by('id')
    idx = find_index(cards, lambda x: x.id == card_id)

    # TODO fix assuming valid id
    if idx > 0:
        neighbors[0] = cards[idx - 1].id
    if idx < len(cards) - 1:
        neighbors[1] = cards[idx + 1].id
    
    return render(request, 'cards/detail.html', {'card': cards[idx], 'prev': neighbors[0], 'next': neighbors[1]})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('card-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
