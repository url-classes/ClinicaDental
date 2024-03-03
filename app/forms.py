from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, Select
from .models import Usuario, TipoUsuario, Dentista, Asistente, Tratamiento, Cita
from .models import Material

class UsuarioSignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de Contraseña', widget=forms.PasswordInput)
    dentista_iddentista = forms.ModelChoiceField(queryset=Dentista.objects.all(), required=False)
    asistente_idasistente = forms.ModelChoiceField(queryset=Asistente.objects.all(), required=False)

    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'password1', 'password2', 'dentista_iddentista', 'tipo_usuario_idtipo_usuario', 'asistente_idasistente']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.password = make_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario


class UsuarioLoginForm(forms.Form):
    nombre_usuario = forms.CharField(label="Nombre de usuario", max_length=45)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def clean(self):
        nombre_usuario = self.cleaned_data.get('nombre_usuario')
        password = self.cleaned_data.get('password')

        if not Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            raise forms.ValidationError("El nombre de usuario no existe.")

        usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
        if not usuario.check_password(password):
            raise forms.ValidationError("La contraseña es incorrecta.")

        return self.cleaned_data
    

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['detalle', 'precio', 'cantidad_citas', 'cita_idcita', 'asistente_idasistente']
    
    def __init__(self, *args, **kwargs):
        super(TratamientoForm, self).__init__(*args, **kwargs)
        # Aplica una clase CSS a todos los campos
        for field in self.fields.values():
            field.widget.attrs['class'] = 'clase'

        self.fields['detalle'].label = "Detalle del Tratamiento"
        self.fields['precio'].label = "Precio"
        self.fields['cantidad_citas'].label = "Cantidad de Citas Necesarias"
        self.fields['cita_idcita'].label = "Cita Asociada"
        self.fields['asistente_idasistente'].label = "Asistente Asignado"

# forms.py
from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['descripcion', 'serie_modelo', 'cantidad', 'precio_individual']
        labels = {
            'descripcion': 'Descripción',
            'serie_modelo': 'Serie/Modelo',
            'cantidad': 'Cantidad',
            'precio_individual': 'Precio Individual',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción'}),
            'serie_modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la serie/modelo'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad'}),
            'precio_individual': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio individual'}),
        }
