from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['original_word', 'translation']
        widgets = {
            'original_word': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter word in foreign language'}),
            'translation': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter translation'}),
        } 