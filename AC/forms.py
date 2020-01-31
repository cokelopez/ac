from django import forms
from .models import Conductores, Propietarios, Carros, Polizas


class PostConductores(forms.ModelForm):
    class Meta:
        model = Conductores
        fields = ('nombres', 'apellidos', 'telefono', 'edad', 'ine')


class EditConductores(forms.ModelForm):
    class Meta:
        model = Conductores
        fields = ('nombres', 'apellidos', 'telefono', 'edad', 'ine')


class PostPropietarios(forms.ModelForm):
    class Meta:
        model = Propietarios
        fields = ('nombres', 'apellidos', 'telefono')


class EditPropietarios(forms.ModelForm):
    class Meta:
        model = Propietarios
        fields = ('nombres', 'apellidos', 'telefono')


class PostCarros(forms.ModelForm):
    class Meta:
        model = Carros
        fields = ('nombre', 'marca', 'modelo', 'year',
                  'placa', 'color', 'conductor', 'propietario')


class EditCarros(forms.ModelForm):
    class Meta:
        model = Carros
        fields = ('nombre', 'marca', 'modelo', 'year',
                  'placa', 'color', 'conductor', 'propietario')


class PostPolizas(forms.ModelForm):
    class Meta:
        model = Polizas
        fields = ('nombre', 'numero', 'carro', 'inicio_poliza',
                  'fin_poliza', 'documento')
        widgets = {'inicio_poliza': forms.DateInput(attrs={'type': 'date'}),
                   'fin_poliza': forms.DateInput(attrs={'type': 'date'})
                   }


class EditPolizas(forms.ModelForm):
    class Meta:
        model = Polizas
        fields = ('nombre', 'numero', 'carro', 'inicio_poliza',
                  'fin_poliza', 'documento')
        widgets = {'inicio_poliza': forms.DateInput(attrs={'type': 'date'}),
                   'fin_poliza': forms.DateInput(attrs={'type': 'date'})
                   }
