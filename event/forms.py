from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'event_nm': forms.TextInput(attrs={'size': 20}),
            'date': forms.DateTimeInput(),
            'place': forms.TextInput(attrs={'size': 50})
        }
