from django import forms
from .models import Paste

class PasteForm(forms.ModelForm):

    class Meta:
        model = Paste
        fields = '__all__'