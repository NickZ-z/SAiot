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

class DeviceFilterForm(forms.Form):
    port_filter = forms.ChoiceField(choices=[('', 'Todos'), ('Aberto', 'Sim'), ('Fechado', 'Nenhuma')], required=False)
    status_filter = forms.ChoiceField(choices=[('', 'Todos'), ('Aberto', 'Aberto'), ('Fechado', 'Fechado')], required=False)
    ip_filter = forms.CharField(max_length=100, required=False)
    room_filter = forms.CharField(max_length=100, required=False)