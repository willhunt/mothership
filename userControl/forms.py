# Get base user class
from django.contrib.auth.models import User
from django import forms

# New user form class based upon Django base user model form
class UserForm(forms.ModelForm):
    # Set password field type
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'mdl-textfield__input'}))

    class Meta:
        # Database model type (we are adding a user)
        model = User
        # Fields for model (same as in user models file)
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        # Add/overide data for models fields
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username', 'class': 'mdl-textfield__input'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'first name', 'class': 'mdl-textfield__input'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name', 'class': 'mdl-textfield__input'}),
            'email': forms.TextInput(attrs={'placeholder': 'email address', 'class': 'mdl-textfield__input'}),
        }

