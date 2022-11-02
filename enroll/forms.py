from django import forms 
from .models import User 


# created form using ModelFormAPI 
class StudentRegistration(forms.ModelForm):
    class Meta:
        model  = User     # import User from models.py
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),   ## using css concept to make it good - looking
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }