from django import forms
from django.forms import ModelForm

from factureTelephonique.models import *

class clientForms(ModelForm):
    class Meta:
        model= Client
        fields = ['nomClient', 'numClient']
        widgets = {
            'nomClient': forms.TextInput(attrs={'class': 'form-control'}),
            'numClient': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CdrFroms(ModelForm):
    class Meta:
        model = Cdr
        fields='__all__'
        widgets = {
            'date': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'}),
        }



class FactureFroms(ModelForm):
    class Meta:
        model = Facture
        fields='__all__'



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class DateInput(forms.DateInput):
     input_type = 'date'