from .models import *
from django import forms

class DoorForm(forms.ModelForm): 
    class Meta:
        model = Door
        fields = '__all__' 
        widgets = {
            'ip' : forms.TextInput(attrs={'class': 'form-control' }),
            'name' : forms.TextInput(attrs={'class': 'form-control' }),
            'status' : forms.TextInput(attrs={'class': 'form-control' }),
            'number_door' : forms.IntegerField(attrs={'class': 'form-control' }),
        }
