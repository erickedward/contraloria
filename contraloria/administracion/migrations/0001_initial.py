# Generated by Django 2.0.4 on 2018-04-23 03:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=40, verbose_name='Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='DevolucionesDinero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=11)),
                ('fecha_devolucion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='EntregasDinero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=11)),
                ('concepto', models.TextField(verbose_name='Concepto')),
                ('fecha_entrega', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.TextField(verbose_name='Concepto')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=11)),
                ('fecha_gasto', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Gasto')),
                ('anulado', models.BooleanField(verbose_name='Gasto Anulado')),
                ('fecha_anulacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('motivo_anulacion', models.CharField(max_length=150, verbose_name='Motivo de Anulación')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_actualizacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField(verbose_name='Monto')),
                ('fecha_limite', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PagosPropietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Pago')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.Pagos')),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=40, verbose_name='Apellido')),
                ('apto', models.CharField(max_length=4, unique='true', verbose_name='Nro de Apartamento')),
                ('telefono', models.CharField(blank=True, max_length=11, null=True, verbose_name='Teléfono')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.Cargos')),
            ],
        ),
        migrations.AddField(
            model_name='pagospropietario',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.Propietario'),
        ),
        migrations.AddField(
            model_name='gastos',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.Propietario'),
        ),
        migrations.AddField(
            model_name='entregasdinero',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.Propietario'),
        ),
        migrations.AddField(
            model_name='devolucionesdinero',
            name='entrega_dinero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administracion.EntregasDinero'),
        ),
    ]
