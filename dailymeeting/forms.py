from django import forms

from .models import Day


class DayForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = ("day", "message", "image1", "image2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['day'].widget.attrs['class'] = 'form-control'
        self.fields['day'].widget.attrs['placeholder'] = '日付'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = '本文'
