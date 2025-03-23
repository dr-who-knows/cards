from django.db import models

# Create your models here.

class Card(models.Model):
    original_word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    
    # For canvas positioning
    x_position = models.IntegerField(default=0)
    y_position = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.original_word} - {self.translation}"
