from django import forms
from .models import Destroy, Furniture

class FurnitureForm(forms.ModelForm):
  class Meta:
    model = Furniture
    fields = ['name', 'color', 'description', 'age']

class DestroyForm(forms.ModelForm):
    class Meta:
        model = Destroy
        fields = ['date', 'supply']
