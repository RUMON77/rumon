from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'email', 'mobile', 'address', 'detail', 'prescription', 'next_visit_date')