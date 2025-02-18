from django import forms
from .models import Car


class CarCreateForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('category', 'title', 'model', 'description', 'year', 'engine_capacity', 'odometer', 'color', 'image')
