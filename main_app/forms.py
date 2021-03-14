from django import forms
from .models import Destroy

class DestroyForm(forms.ModelForm):
    class Meta:
        model = Destroy
        fields = ['date', 'supply']
