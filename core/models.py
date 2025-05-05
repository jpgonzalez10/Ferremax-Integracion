from django.db import models

# Create your models here.
class Genero(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    

class Rol(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    

class Usuarios(models.Model):
    rut_user = models.CharField(max_length=10, primary_key=True)
    nombre_user = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    s_apellido = models.CharField(max_length=50)
    correo_user = models.EmailField(max_length=50)
    contrasena_user = models.CharField(max_length=50)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_user} {self.p_apellido}"

class Marca(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    
class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField()
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    id_tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto
    
class EstadoPago(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    
class MedioPago(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    
class Region(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Sucursal(models.Model):
    direccion = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.direccion
    
class Pedido(models.Model):
    fecha_pedido = models.DateField()
    rut_user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido #{self.id}"
    
class ProductoPedido(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Pedido {self.id_pedido} - Producto {self.id_producto}"
    
class Pago(models.Model):
    fecha_pago = models.DateField()
    monto_pagar = models.IntegerField()
    id_medio_pago = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
    id_estado_pago = models.ForeignKey(EstadoPago, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago #{self.id}"
    
class Inventario(models.Model):
    ubicacion = models.CharField(max_length=50)
    fecha_ultima_actualizacion = models.DateField()

    def __str__(self):
        return self.ubicacion