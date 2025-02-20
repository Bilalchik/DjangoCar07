from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('category', 'title', 'model', 'description', 'year', 'engine_capacity', 'odometer', 'color', 'image')
