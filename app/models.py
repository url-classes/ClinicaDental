# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alergia(models.Model):
    idalergia = models.IntegerField(db_column='idAlergia', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alergia'


class AlergiaHasPaciente(models.Model):
    alergia_idalergia = models.OneToOneField(Alergia, models.DO_NOTHING, db_column='Alergia_idAlergia', primary_key=True)  # Field name made lowercase. The composite primary key (Alergia_idAlergia, Paciente_idPaciente) found, that is not supported. The first column is selected.
    paciente_idpaciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='Paciente_idPaciente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alergia_has_paciente'
        unique_together = (('alergia_idalergia', 'paciente_idpaciente'),)


class Asistente(models.Model):
    idasistente = models.IntegerField(db_column='idAsistente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    escolaridad = models.CharField(max_length=45, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asistente'


class Cita(models.Model):
    idcita = models.IntegerField(db_column='idCita', primary_key=True)  # Field name made lowercase.
    fecha_propuesta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cita'


class Dentista(models.Model):
    iddentista = models.IntegerField(db_column='idDentista', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    numero_telefono = models.CharField(max_length=45, blank=True, null=True)
    correo_electronico = models.CharField(max_length=45, blank=True, null=True)
    no_colegiado = models.CharField(max_length=45, blank=True, null=True)
    tipo_especialidad_idtipo_especialidad = models.ForeignKey('TipoEspecialidad', models.DO_NOTHING, db_column='Tipo_Especialidad_idTipo_Especialidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dentista'


class DentistaHasTratamiento(models.Model):
    dentista_iddentista = models.OneToOneField(Dentista, models.DO_NOTHING, db_column='Dentista_idDentista', primary_key=True)  # Field name made lowercase. The composite primary key (Dentista_idDentista, Tratamiento_idTratamientno) found, that is not supported. The first column is selected.
    tratamiento_idtratamientno = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='Tratamiento_idTratamientno')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dentista_has_tratamiento'
        unique_together = (('dentista_iddentista', 'tratamiento_idtratamientno'),)


class Factura(models.Model):
    idfactura = models.IntegerField(db_column='idFactura', primary_key=True)  # Field name made lowercase.
    detalle = models.CharField(max_length=45, blank=True, null=True)
    cantidad_servicios = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    tratamiento_idtratamientno = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='Tratamiento_idTratamientno')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura'


class Material(models.Model):
    idmaterial = models.IntegerField(db_column='idMaterial', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    serie_modelo = models.CharField(max_length=45, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_individual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material'


class Paciente(models.Model):
    idpaciente = models.IntegerField(db_column='idPaciente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    numero_telefonico = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    numero_seguro = models.CharField(max_length=45, blank=True, null=True)
    cita_idcita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='Cita_idCita')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paciente'


class TipoEspecialidad(models.Model):
    idtipo_especialidad = models.IntegerField(db_column='idTipo_Especialidad', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_especialidad'


class TipoUsuario(models.Model):
    idtipo_usuario = models.IntegerField(db_column='idTipo_Usuario', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    permisos = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Tratamiento(models.Model):
    idtratamientno = models.IntegerField(db_column='idTratamientno', primary_key=True)  # Field name made lowercase.
    detalle = models.CharField(max_length=45, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    cantidad_citas = models.IntegerField(blank=True, null=True)
    cita_idcita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='Cita_idCita')  # Field name made lowercase.
    asistente_idasistente = models.ForeignKey(Asistente, models.DO_NOTHING, db_column='Asistente_idAsistente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tratamiento'


class TratamientoHasMaterial(models.Model):
    tratamiento_idtratamientno = models.OneToOneField(Tratamiento, models.DO_NOTHING, db_column='Tratamiento_idTratamientno', primary_key=True)  # Field name made lowercase. The composite primary key (Tratamiento_idTratamientno, Material_idMaterial) found, that is not supported. The first column is selected.
    material_idmaterial = models.ForeignKey(Material, models.DO_NOTHING, db_column='Material_idMaterial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tratamiento_has_material'
        unique_together = (('tratamiento_idtratamientno', 'material_idmaterial'),)


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombre_usuario = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    dentista_iddentista = models.ForeignKey(Dentista, models.DO_NOTHING, db_column='Dentista_idDentista')  # Field name made lowercase.
    tipo_usuario_idtipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='Tipo_Usuario_idTipo_Usuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
