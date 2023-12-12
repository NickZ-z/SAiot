from .models import *
from django import forms

class DoorForm(forms.ModelForm): 
    class Meta:
        model = Door
        fields = ['name', 'number_door', 'device'] 
        labels = {
            'name': 'Nome',
            'number_door': 'Número da Porta',
            'device': ' Função do Dispositivo',
        }
        
    def __init__(self, *args, **kwargs):
            super(DoorForm, self).__init__(*args, **kwargs)
            self.fields['device'].queryset = Device.objects.all()