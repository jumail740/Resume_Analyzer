from django import forms
from .models import ResumeAnalysis

class ResumeForm(forms.ModelForm):
    class Meta:
        model=ResumeAnalysis
        fields=['resume','job_description']