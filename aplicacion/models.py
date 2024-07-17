from django.db import models


class Hotel(models.Model):
    nombre = models.CharField(max_length=30,  null=False)
    ubicacion = models.CharField(max_length=30)
    cantidad_habitaciones = models.IntegerField
    capacidad_total = models.IntegerField

    def __str__(self):
        return f"{self.nombre} {self.ubicacion}"


class TipoServicio(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.nombre}"


class Servicio(models.Model):
    valor = models.FloatField()
    descripcion = models.CharField(max_length=300)
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_servicio} - {self.hotel} - {self.valor}"


class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)



class Habitacion(models.Model):
    numero = models.IntegerField()
    valor = models.FloatField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    cantidad_personas = models.IntegerField()
    cantidad_banos = models.IntegerField()
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, default="Suite")



class Pasajero(models.Model):
    nombre = models.CharField(max_length=30,  null=False)
    apellido = models.CharField(max_length=30,  null=False)
    correo = models.EmailField(default=("correo@correo.cl"))
    numero = models.IntegerField(default=12345678)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


class HabitacionReserva(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.pasajero} {self.habitacion}"


class Reserva(models.Model):
    fecha_inicio = models.DateField(null=True)
    fecha_final = models.DateField(null=True)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)


class HistorialPrecios(models.Model):
    fecha_inicio = models.DateField(null=True)
    fecha_final = models.DateField(null=True)
    valor = models.FloatField(null=True)

    def __str__(self):
        return f"{self.fecha_inicio} - {self.fecha_final} - {self.valor}"


class Administrador(models.Model):
    nombre = models.CharField(max_length=30,  null=False)
    apellido = models.CharField(max_length=30,  null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Oferta(models.Model):
    fecha_inicio = models.DateField(null=True)
    fecha_final = models.DateField(null=True)
    porcentaje_dcto = models.IntegerField(null=True)


class OfertaReserva(models.Model):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)


class OfertaServicio(models.Model):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    capacidad = models.IntegerField()
    ingresos = models.FloatField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.hotel.nombre}"
