from django import forms
from django.contrib.auth.hashers import make_password
from django.forms import ModelForm, Select
from .models import Usuario, TipoUsuario, Dentista, Asistente, Tratamiento, Cita, Material, TipoEspecialidad, Paciente
from django import forms

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
        labels = {
            'detalle': 'Detalle',
            'precio': 'Precio',
            'cantidad_citas': 'Cantidad de Citas',
            'cita_idcita': 'Identificador de la Cita',
            'asistente_idasistente': 'Identificador del Asistente'
        }
        widgets = {
            'detalle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la el detalle'}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio'}),
            'cantidad_citas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad de citas'}),
            'cita_idcita': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el identificador de la cita'}),
            'asistente_idasistente': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el identificador del asistente'}),
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['descripcion', 'serie_modelo', 'cantidad', 'precio_individual']
        labels = {
            'descripcion': 'Descripción',
            'serie_modelo': 'Tipo',
            'cantidad': 'Cantidad',
            'precio_individual': 'Precio Individual',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción'}),
            'serie_modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el tipo'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad'}),
            'precio_individual': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio individual'}),
        }

class DentistaForm(forms.ModelForm):
    class Meta:
        model = Dentista
        tipo_especalidad_idtipo_especialidad = forms.ModelChoiceField(queryset=TipoEspecialidad.objects.all(), required=False)
        fields = ['nombre', 'apellido', 'numero_telefono', 'correo_electronico', 'no_colegiado', 'tipo_especialidad_idtipo_especialidad']
        labels = {
            'nombre': 'Nombre', 
            'apellido': 'Apellido', 
            'numero_telefono': 'Número Teléfono', 
            'correo_electronico': 'Correo Electrónico', 
            'no_colegiado': 'Número de Colegiado', 
            'tipo_especialidad_idtipo_especialidad': 'Especialidad'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'numero_telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de teléfono'}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electrónico'}),
            'no_colegiado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de colegiado'}),
        }
    
class AsistenteForm(forms.ModelForm):
    class Meta:
        model = Asistente
        fields = ['nombre', 'apellido', 'escolaridad', 'salario']
        labels = {
            'nombre': 'Nombre', 
            'apellido': 'Apellido', 
            'escolaridad': 'Escolaridad', 
            'salario': 'Salario', 
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'escolaridad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su escolaridad'}),
            'salario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el salario'}),
        }
class TratamientoMaterialForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        materiales = Material.objects.all()
        for material in materiales:
            self.fields[f'material_seleccionado_{material.idmaterial}'] = forms.BooleanField(label=f"Utilizar {material.descripcion}", required=False)
            self.fields[f'cantidad_{material.idmaterial}'] = forms.IntegerField(label=f"Cantidad para {material.descripcion}", min_value=1, required=False)

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'numero_telefonico', 'correo_electronico', 'edad', 'numero_seguro']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'numero_telefonico': 'Numero de Telefono',
            'correo_electronico': 'Correo Electronico',
            'edad': 'Edad',
            'numero_seguro': 'Numero de Seguro',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'numero_telefonico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el numero telefonico'}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el correo electronico'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la edad'}),
            'numero_seguro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el numero de seguro'}),
        }

class CitasForm(forms.ModelForm):
    paciente_idpaciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(), 
        required=False,
        label='ID Paciente',  
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Cita
        fields = ['idcita', 'paciente_idpaciente', 'fecha_propuesta'] 
        labels = {
            'idcita': 'ID Cita',
            'fecha_propuesta': 'Fecha Propuesta',
        }
        widgets = {
            'fecha_propuesta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha propuesta'})
        }