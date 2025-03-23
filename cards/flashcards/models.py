from django.db import models
from django.contrib.auth.models import User

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
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Canvas view settings
    canvas_translate_x = models.IntegerField(default=0)
    canvas_translate_y = models.IntegerField(default=0)
    canvas_scale = models.FloatField(default=1.0)
    
    def __str__(self):
        return f"Profile for {self.user.username}"
