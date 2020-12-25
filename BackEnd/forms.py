from django import forms
from .models import *


class PrisonerForm(forms.ModelForm):

    class Meta:
        model = Prisoner
        fields = '__all__'
