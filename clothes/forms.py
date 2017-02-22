from django import forms

from .models import Clothing

class ClothingForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields = ('name', 'clothing_type', 'image')
