from django.db import models

# Modelo cliente.

class Cliente(models.Model):
    cli_nombre = models.CharField(max_length=100, verbose_name='Cliente')
    cli_celular = models.CharField(max_length=20, verbose_name='Celular')
    cli_correo = models.EmailField(verbose_name='Correo')
    cli_direccion = models.CharField(max_length=200, verbose_name='Dirección')
    cli_ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    cli_created_at = models.DateTimeField(auto_created=True, verbose_name='Creado el')

    def __str__(self):
        return self.cli_nombre

# Modelo producto.

class Producto(models.Model):
    pro_nombre = models.CharField(max_length=100, verbose_name='Producto')
    pro_cantidad = models.IntegerField(verbose_name='Cantidad')
    pro_created_at = models.DateTimeField(auto_created=True, verbose_name='Creado el')

    def __str__(self):
        return self.pro_nombre

# Modelo pedido.

class Pedido(models.Model):
    ESTADOS_PEDIDO = (
        ('pendiente', 'Pendiente'),
        ('en_ruta', 'En ruta'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    )

    REGLA_ENVIO = (
        ('domicilio', 'Domicilio'),
        ('recoge', 'Recoge en punto'),
    )

    ped_id = models.AutoField(primary_key=True, editable=False)
    ped_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    ped_items = models.ManyToManyField(Producto, verbose_name='Detalle de productos')
    ped_fecha = models.DateField(verbose_name='Fecha del pedido')
    ped_estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, verbose_name='Estado')
    ped_pagado = models.BooleanField(verbose_name='Pagado?')
    ped_regla_envio = models.CharField(max_length=20, choices=REGLA_ENVIO, verbose_name='Forma de entrega')
    ped_observaciones = models.TextField(verbose_name='Observaciones')
    ped_created_at = models.DateTimeField(auto_created=True, verbose_name='Creado el')

    def __str__(self):
        return f'{self.ped_id}, {self.ped_fecha}, {self.ped_cliente.cli_nombre}'
