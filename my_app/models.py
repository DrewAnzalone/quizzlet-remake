from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Card(models.Model):
    hint = models.TextField(max_length=255)
    answer = models.CharField(max_length=127)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.hint} : {self.answer}"
    
    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'card_id': self.id})
    