from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['original_word', 'translation']
        widgets = {
            'original_word': forms.TextInput(attrs={'class': 'form-control'}),
            'translation': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add form-control class to all fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
            
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add form-control class to all fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control' 