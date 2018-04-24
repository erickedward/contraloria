from django.db import models
from django.utils import timezone

class Cargos(models.Model):
    cargo = models.CharField(max_length = 40,verbose_name='Cargo')

    def __str__(self):
        return '%s'%(self.cargo)

class Propietario(models.Model):
    nombre = models.CharField(max_length = 40,verbose_name='Nombre')
    apellido = models.CharField(max_length = 40,verbose_name='Apellido')
    apto = models.CharField(max_length = 4,verbose_name='Nro de Apartamento',unique='true')
    telefono = models.CharField(max_length = 11,verbose_name='Teléfono',blank=True, null=True)
    cargo = models.ForeignKey(Cargos, null=False, blank=False, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s: %s %s (%s)'%(self.apto, self.apellido, self.nombre, self.cargo)


class Pagos(models.Model):
    monto = models.IntegerField(verbose_name='Monto')
    fecha_limite = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s'%(self.fecha_limite)

class PagosPropietario(models.Model):
    propietario = models.ForeignKey(Propietario, null=False, blank=False, on_delete=models.PROTECT)
    pago = models.ForeignKey(Pagos, null=False, blank=False, on_delete=models.PROTECT)
    fecha_pago = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Pago')

class Gastos(models.Model):
    concepto = models.TextField(verbose_name='Concepto')
    monto = models.DecimalField(max_digits=11,decimal_places=2)
    responsable = models.ForeignKey(Propietario, null=False, blank=False, on_delete=models.PROTECT)
    fecha_gasto = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Gasto')
    anulado = models.BooleanField(verbose_name='Gasto Anulado')
    fecha_anulacion = models.DateTimeField(default=timezone.now)
    motivo_anulacion = models.CharField(max_length = 150,verbose_name='Motivo de Anulación')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(default=timezone.now)

class EntregasDinero(models.Model):
    propietario = models.ForeignKey(Propietario, null=False, blank=False, on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=11,decimal_places=2)
    concepto = models.TextField(verbose_name='Concepto')
    fecha_entrega = models.DateTimeField(default=timezone.now)

class DevolucionesDinero(models.Model):
    entrega_dinero = models.ForeignKey(EntregasDinero, null=False, blank=False,on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=11,decimal_places=2)
    fecha_devolucion = models.DateTimeField(default=timezone.now)


