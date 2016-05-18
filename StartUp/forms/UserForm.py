from django import forms

# Create your models here.

class User(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=4)