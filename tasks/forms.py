from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['Titulo', 'Recepcion', 'Generacion', 'Entregado']
        widgets = {
            'Titulo': forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Escribe un titulo'} ),
            'Entregado': forms.CheckboxInput(attrs={"class": 'form-check-input m-auto'} ),
        }