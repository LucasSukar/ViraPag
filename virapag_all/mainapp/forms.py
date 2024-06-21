
from django import forms

class LivroSearchForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False)
    autor = forms.CharField(max_length=100, required=False)
    
