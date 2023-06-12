from django import forms


class aplicacionForm(forms.Form):
    nombre = forms.CharField()
    clave = forms.CharField()