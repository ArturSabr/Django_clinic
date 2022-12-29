from django import forms
from .models import *

class EntryForm(forms.ModelForm):
   # date = forms.DateTimeField(
    #    widget=forms.TextInput(
     #       attrs={'type': 'date'}
      #  )
    #)
    class Meta:
        model = Entry
        fields = '__all__'
