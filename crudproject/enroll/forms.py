from wsgiref.validate import validator
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentRegistration, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['email'].required = False

    class Meta:
        model = User 
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
  
        }