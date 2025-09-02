from django import forms
from travel_explorer.models import nature
class natureform(forms.ModelForm):
    class Meta:
        model= nature
        Fields = '__all__'