from django import forms
from django.contrib.auth.models import User
from .models import Livro

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao']

class PreferenciasForm(forms.Form):
    cor_fundo = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
