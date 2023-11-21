from .models import *
from django import forms

class DoorForm(forms.ModelForm): 
    class Meta:
        model = Door
        fields = '__all__' 
        widgets = {
            'ip' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira o endereço'}),
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira o nome' }),
            'status' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira s status' }),
            'number_door' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Insira número' }),
        }
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'}),
        }