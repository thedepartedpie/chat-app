from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
        label='Username',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
        label='Password',
    )

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegistrationForbm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
            'email': forms.EmailInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
            'password1': forms.PasswordInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
            'password2': forms.PasswordInput(attrs={'class': 'bg-gray-100 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-300 w-full transition duration-150 ease-in-out'}),
        }