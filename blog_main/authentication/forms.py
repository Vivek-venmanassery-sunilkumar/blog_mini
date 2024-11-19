from django import forms
from django .contrib.auth.models import User
from django.core.exceptions import ValidationError  

class SignupForm(forms.ModelForm):
    full_name = forms.CharField(max_length=150, required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password') 
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned_data