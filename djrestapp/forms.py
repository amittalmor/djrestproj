from django import forms
from .models import GeoAddress


class GeoAddressForm(forms.ModelForm):
    class Meta:
        model = GeoAddress
        fields = ['country','city','street']
        widgets = {
            'country': forms.TextInput(
                attrs={'id': 'country-text', 'required': 'True', 'placeholder': 'Enter a country name...'}
            ),
            'city': forms.TextInput(
                attrs={'id': 'city-text', 'placeholder': 'Enter a city name...'}
            ),
            'street': forms.TextInput(
                attrs={'id': 'street-text', 'placeholder': 'Enter a street name...'}
            ),               
        }
