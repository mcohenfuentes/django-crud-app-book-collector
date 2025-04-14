from django import forms
from datetime import date
from .models import Reading

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = ['date', 'status', 'notes']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'max': date.today().isoformat()
                }
            ),
        }