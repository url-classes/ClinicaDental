# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import check_password as django_check_password
from django.utils.timezone import now

class Alergia(models.Model):
    idalergia = models.AutoField(db_column='idAlergia', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'alergia'
        
    def __str__(self):
        return f"{self.idalergia} {self.descripcion}"


class AlergiaPaciente(models.Model):
    alergia_idalergia = models.OneToOneField(Alergia, models.DO_NOTHING, db_column='Alergia_idAlergia', primary_key=True)  # Field name made lowercase. The composite primary key (Alergia_idAlergia, Paciente_idPaciente) found, that is not supported. The first column is selected.
    paciente_idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='Paciente_idPaciente')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'alergia_paciente'
        unique_together = (('alergia_idalergia', 'paciente_idpaciente'),)
        
    def __str__(self):
        return f"{self.alergia_idalergia} - {self.paciente_idpaciente.nombre}"


class Asistente(models.Model):
    idasistente = models.AutoField(db_column='idAsistente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    escolaridad = models.CharField(max_length=45, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    estado = models.BooleanField(default=True, null=True, blank=True)
    url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asistente'
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cita(models.Model):
    idcita = models.AutoField(db_column='idCita', primary_key=True)  # Field name made lowercase.
    fecha_propuesta = models.DateTimeField(blank=True, null=True)
    estado = models.BooleanField(default=True, null=True, blank=True)
    paciente_idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='paciente_idPaciente')

    class Meta:
        managed = True
        db_table = 'cita'
        
    def __str__(self):
        return f"{self.idcita} {self.fecha_propuesta}"


class Dentista(models.Model):
    iddentista = models.AutoField(db_column='idDentista', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    numero_telefono = models.CharField(max_length=45, blank=True, null=True)
    correo_electronico = models.CharField(max_length=45, blank=True, null=True)
    no_colegiado = models.CharField(max_length=45, blank=True, null=True)
    estado = models.BooleanField(default=True, null=True, blank=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    tipo_especialidad_idtipo_especialidad = models.ForeignKey('TipoEspecialidad', models.DO_NOTHING, db_column='Tipo_Especialidad_idTipo_Especialidad')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'dentista'
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class DentistaTratamiento(models.Model):
    dentista_iddentista = models.OneToOneField(Dentista, models.DO_NOTHING, db_column='Dentista_idDentista', primary_key=True)  # Field name made lowercase. The composite primary key (Dentista_idDentista, Tratamiento_idTratamientno) found, that is not supported. The first column is selected.
    tratamiento_idtratamientno = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='Tratamiento_idTratamientno')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'dentista_tratamiento'
        unique_together = (('dentista_iddentista', 'tratamiento_idtratamientno'),)
        
    def __str__(self):
        return f"{self.dentista_iddentista} {self.tratamiento_idtratamientno}"


class Factura(models.Model):
    idfactura = models.AutoField(db_column='idFactura', primary_key=True)  # Field name made lowercase.
    detalle = models.CharField(max_length=45, blank=True, null=True)
    cantidad_servicios = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    tratamiento_idtratamientno = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='Tratamiento_idTratamientno')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'factura'
        
    def __str__(self):
        return f"{self.idfactura} {self.detalle} {self.cantidad_servicios} {self.fecha} {self.total} {self.tratamiento_idtratamientno}"


class Material(models.Model):
    idmaterial = models.AutoField(db_column='idMaterial', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    serie_modelo = models.CharField(max_length=45, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_individual = models.FloatField(blank=True, null=True)
    estado = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'material'
        
    def __str__(self):
        return f"{self.idmaterial} {self.descripcion} {self.serie_modelo} {self.cantidad} {self.precio_individual}"


class Paciente(models.Model):
    idpaciente = models.AutoField(db_column='idPaciente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    numero_telefonico = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    numero_seguro = models.CharField(max_length=45, blank=True, null=True)
    correo_electronico = models.EmailField(max_length=254, blank=True, null=True)
    ultima_visita = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'paciente'
        
    def __str__(self):
        return f"{self.idpaciente} {self.nombre} {self.apellido} {self.numero_telefonico} {self.edad} {self.numero_seguro}"


class TipoEspecialidad(models.Model):
    idtipo_especialidad = models.AutoField(db_column='idTipo_Especialidad', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_especialidad'
        
    def __str__(self):
        return f"{self.idtipo_especialidad} {self.descripcion}"


class TipoUsuario(models.Model):
    idtipo_usuario = models.AutoField(db_column='idTipo_Usuario', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    permisos = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_usuario'
        
    def __str__(self):
        return f"{self.descripcion} {self.permisos}"


class Tratamiento(models.Model):
    idtratamientno = models.AutoField(db_column='idTratamientno', primary_key=True)  # Field name made lowercase.
    detalle = models.CharField(max_length=45, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    cantidad_citas = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField(default=True, null=True, blank=True)
    cita_idcita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='Cita_idCita')  # Field name made lowercase.
    asistente_idasistente = models.ForeignKey(Asistente, models.DO_NOTHING, db_column='Asistente_idAsistente')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tratamiento'
        
    def __str__(self):
        return f"{self.idtratamientno} {self.detalle} {self.precio} {self.cantidad_citas} {self.cita_idcita} {self.asistente_idasistente}"


class TratamientoMaterial(models.Model):
    id = models.AutoField(primary_key=True) 
    tratamiento_idtratamientno = models.ForeignKey(Tratamiento, models.DO_NOTHING, db_column='Tratamiento_idTratamientno')  # Se cambia a ForeignKey
    material_idmaterial = models.ForeignKey(Material, models.DO_NOTHING, db_column='Material_idMaterial')  # Sin cambios
    cantidad_utilizada = models.IntegerField(blank=True, null=True)
    cantidad_antes = models.IntegerField(null=True, blank=True, default=None)
    cantidad_despues = models.IntegerField(null=True, blank=True, default=None)
    fecha_transaccion = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'tratamiento_material'
        unique_together = (('tratamiento_idtratamientno', 'material_idmaterial'),)  
        
    def __str__(self):
        return f"{self.tratamiento_idtratamientno} {self.material_idmaterial} {self.cantidad_utilizada}"


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)
    nombre_usuario = models.CharField(max_length=45)
    password = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    intentos_fallidos = models.IntegerField(default=0, blank=True, null=True)
    tiempo_bloqueo = models.DateTimeField(blank=True, null=True)
    dentista_iddentista = models.ForeignKey(Dentista, on_delete=models.DO_NOTHING, db_column='Dentista_idDentista', blank=True, null=True)
    tipo_usuario_idtipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, db_column='Tipo_Usuario_idTipo_Usuario')
    asistente_idasistente = models.ForeignKey(Asistente, on_delete=models.DO_NOTHING, db_column='Asistente_idAsistente', blank=True, null=True)

    
    
    class Meta:
        managed = True
        db_table = 'usuario'
        
    def check_password(self, raw_password):
        return django_check_password(raw_password, self.password)
    
    def is_authenticated(self):
        return True
    
    def has_permiso(self, permiso_requerido):
        if self.tipo_usuario_idtipo_usuario.permisos:
            permisos_usuario_lista = self.tipo_usuario_idtipo_usuario.permisos.split(',')
            return permiso_requerido.strip() in permisos_usuario_lista
        return False
        
    def __str__(self):
        return f"{self.idusuario} {self.nombre_usuario} {self.password} {self.dentista_iddentista} {self.tipo_usuario_idtipo_usuario} {self.asistente_idasistente}"
