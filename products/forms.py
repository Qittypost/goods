from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']
        widgets = {
            'author': forms.TextInput(attrs={'maxlength': 100}),
            'text': forms.Textarea(),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }
