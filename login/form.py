from django import forms



class UserForm(forms.Form):
    username = forms.CharField(label="id", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))