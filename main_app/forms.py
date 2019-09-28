from django import forms

class AutoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length= 100)
    precio = forms.DecimalField(label= 'precio', max_digits= 10, decimal_places= 2)
    color = forms.CharField(label= 'color', max_length= 100)
    modelo = forms.CharField(label = 'modelo', max_length= 100)
    img_url = forms.CharField(label = 'imagen URL')