from django import forms
from .models import Paste

# Defines the fields we don't want to render on a form...
invalid_fields = ['created_at', 'user']

class PasteForm(forms.ModelForm):

    class Meta:

        model = Paste

        fields = [field.name for field in Paste._meta.fields if field.name not in invalid_fields]