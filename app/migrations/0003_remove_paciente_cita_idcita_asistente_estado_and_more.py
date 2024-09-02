# Generated by Django 5.1 on 2024-09-02 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cita_paciente_idpaciente_usuario_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='cita_idcita',
        ),
        migrations.AddField(
            model_name='asistente',
            name='estado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='asistente',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cita',
            name='estado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dentista',
            name='estado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dentista',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='estado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='correo_electronico',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='ultima_visita',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='estado',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='tratamientomaterial',
            name='cantidad_antes',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tratamientomaterial',
            name='cantidad_despues',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='tratamientomaterial',
            name='fecha_transaccion',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='intentos_fallidos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tiempo_bloqueo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='asistente_idasistente',
            field=models.ForeignKey(blank=True, db_column='Asistente_idAsistente', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.asistente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dentista_iddentista',
            field=models.ForeignKey(blank=True, db_column='Dentista_idDentista', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.dentista'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
