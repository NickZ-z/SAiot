from .models import *
from django import forms

class DoorForm(forms.ModelForm): 
    class Meta:
        model = Door
        fields = ['name', 'mac', 'number_door', 'device'] 
        
    def __init__(self, *args, **kwargs):
            super(DoorForm, self).__init__(*args, **kwargs)
            self.fields['device'].queryset = Device.objects.all()