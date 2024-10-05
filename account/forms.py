import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

from account.models import StudentLog, User

class AccountDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'department', 'mat_no']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'John Doe', 
                'class': 'input input-bordered w-full'
            }),
            'department': forms.TextInput(attrs={
                'placeholder': 'Computer Science', 
                'class': 'input input-bordered w-full'
            }),
            'mat_no': forms.TextInput(attrs={
                'placeholder': '123456', 
                'class': 'input input-bordered w-full'
            }),
        }

class CustomLoginForm(forms.Form):
    mat_no = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Your Matric Number',
            'id': 'mat_no',
            'required': 'required'
        }),
        label="Matriculation Number"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Password',
            'id': 'password',
            'required': 'required'
        }),
        label="Password"
    )

    def clean(self):
        mat_no = self.cleaned_data.get('mat_no')
        password = self.cleaned_data.get('password')
        user = authenticate(mat_no=mat_no, password=password)
        
        if user is None:
            raise forms.ValidationError('Invalid matriculation number or password.')
        
        return self.cleaned_data

class PasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Enter your password',
            'id': 'password',
            'required': 'required'
        }),
        label="Password",
        max_length=100,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Confirm your password',
            'id': 'confirmPassword',
            'required': 'required'
        }),
        label="Confirm Password",
        max_length=100,
    )

    # Validate if password meets the criteria
    def clean_password(self):
        password = self.cleaned_data.get('password')
        name = "John Doe"  # Replace this with actual user input dynamically
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
            raise ValidationError('Password must contain both letters and numbers.')
        if not re.search(r'[!@#$%^&*()]', password):
            raise ValidationError('Password must contain at least one special character (!@#$%^&*()).')
        if name.lower() in password.lower():
            raise ValidationError('Password must not contain your name.')
        return password

    # Ensure that both passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError('Passwords do not match.')

class StudentLogForm(forms.ModelForm):
     class Meta:
        model = StudentLog
        fields = ['date', 'entry']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'input input-bordered', 'type': 'date'}),
            'entry': forms.Textarea(attrs={'class': 'textarea textarea-bordered h-24', 'required': True}),
        }