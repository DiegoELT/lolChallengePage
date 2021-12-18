from django import forms

class login(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.PasswordInput(label = 'password', max_length = 20)

class Register(forms.ModelForm):
    username = forms.CharField(label='username', max_length=100)
    password = forms.PasswordInput(label = 'password', max_length = 20)
    riot_id = forms.CharField(max_length=100)
    summoner_name = forms.CharField(max_length=20)
