from django.db import models
from django.urls import reverse

class Card(models.Model):
    hint = models.TextField(max_length=255)
    answer = models.CharField(max_length=127)
    
    def __str__(self):
        return f"{self.hint} : {self.answer}"
    
    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'card_id': self.id})
    