# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CentroEscolar(models.Model):
    id_centro = models.SmallIntegerField(primary_key=True)
    id_muni = models.ForeignKey('Municipio', models.PROTECT, db_column='id_muni', blank=True, null=True)
    id_dep = models.SmallIntegerField(blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.PROTECT, db_column='id_usuario', blank=True, null=True)
    nombre_centro = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono_centro = models.CharField(max_length=20, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    telefono_direc = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'centro_escolar'


class Departamento(models.Model):
    id_dep = models.SmallIntegerField(primary_key=True)
    nombre_dep = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'departamento'


class EstadoProyecto(models.Model):
    id_estado = models.SmallIntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'estado_proyecto'


class Municipio(models.Model):
    id_muni = models.SmallIntegerField(primary_key=True)
    id_dep = models.ForeignKey(Departamento, models.PROTECT, db_column='id_dep')
    nombre_muni = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'municipio'
        unique_together = (('id_muni', 'id_dep'),)


class Prioridad(models.Model):
    id_priori = models.SmallIntegerField(primary_key=True)
    nombre_prioridad = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'prioridad'


class Proveedores(models.Model):
    id_proveedor = models.SmallIntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.PROTECT, db_column='id_usuario', blank=True, null=True)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proveedores'


class ProveedorProyecto(models.Model):
    id_proyecto = models.ForeignKey('Proyectos', models.PROTECT, db_column='id_proyecto', primary_key=True)
    id_proveedor = models.ForeignKey('Proveedores', models.PROTECT, db_column='id_proveedor')
    id_estado = models.ForeignKey(EstadoProyecto, models.PROTECT, db_column='id_estado', blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    costo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    numero_tareas = models.IntegerField(blank=True, null=True)
    tarea_actual = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proveedor_proyecto'
        unique_together = (('id_proyecto', 'id_proveedor'),)


class Proyectos(models.Model):
    id_proyecto = models.SmallIntegerField(primary_key=True)
    id_centro = models.ForeignKey(CentroEscolar, models.PROTECT, db_column='id_centro', blank=True, null=True)
    id_priori = models.ForeignKey(Prioridad, models.PROTECT, db_column='id_priori', blank=True, null=True)
    nombre_proyecto = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    tiempo_estimado = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proyectos'


class Roles(models.Model):
    id_rol = models.SmallIntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'roles'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    id_rol = models.ForeignKey(Roles, models.PROTECT, db_column='id_rol', blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    institucion = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    contrasenia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usuario'
