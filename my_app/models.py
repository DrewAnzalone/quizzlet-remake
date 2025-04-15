from django.db import models

class Card(models.Model):
    hint = models.TextField(max_length=255)
    answer = models.CharField(max_length=127)
    
    def __str__(self):
        return f"{self.hint} : {self.answer}"