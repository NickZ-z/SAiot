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
            'number_door': forms.TextInput(attrs={'class': 'form-control'}),

        }
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'}),
        }