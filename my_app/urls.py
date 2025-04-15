from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.card_index, name='card-index'),
    path('cards/<int:card_id>/', views.card_view, name='card-view'),
    path('cards/create/', views.CardCreate.as_view(), name='card-create'),
]
