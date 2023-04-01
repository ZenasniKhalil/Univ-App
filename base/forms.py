from .models import Etudiant
from django.forms import ModelForm
from django import forms

class FilterForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'
        widgets={
            'niveau':forms.Select(attrs={'class':'form-control'}),
            'domaine':forms.Select(attrs={'class':'form-control'}),
            'filiere':forms.Select(attrs={'class':'form-control'}),
        }