from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from django.core.exceptions import ValidationError
# Create your models here.


class Conductores(models.Model):

    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    edad = models.IntegerField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # validators should be a list
    telefono = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    ine = models.FileField(upload_to='INE/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('nombres', 'apellidos')
        verbose_name_plural = "Conductores"

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

    def get_absolute_url(self):
        return reverse('conductores')


class Propietarios(models.Model):

    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # validators should be a list
    telefono = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('nombres', 'apellidos')
        verbose_name_plural = "Propietarios"

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

    def get_absolute_url(self):
        return reverse('propietarios')


class Carros(models.Model):

    nombre = models.CharField(max_length=20, blank=True, null=True)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    year = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=10)
    conductor = models.ForeignKey(
        Conductores, on_delete=models.SET_NULL, blank=True, null=True)
    propietario = models.ForeignKey(Propietarios, on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=False, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vehículos"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('carros')


class Polizas(models.Model):

    nombre = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=30, unique=True)
    carro = models.ForeignKey(
        Carros, on_delete=models.CASCADE, blank=True, null=True)
    inicio_poliza = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    fin_poliza = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    documento = models.FileField(upload_to='polizas/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Polizas"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('polizas')


class TipoGasto(models.Model):

    nombre = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Tipos de Gasto"

    def __str__(self):
        return self.nombre


class Gasto(models.Model):

    monto = models.DecimalField(max_digits=6, decimal_places=2)
    iva = models.BooleanField()
    fecha = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    factura = models.FileField(upload_to='facturas/', blank=True, null=True)
    gasto = models.ForeignKey(TipoGasto, on_delete=models.PROTECT)
    carro = models.ForeignKey(
        Carros, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Gastos'
        ordering = ['fecha']

    def get_absolute_url(self):
        return reverse('gasto')


class Renta(models.Model):

    nombre = models.CharField(max_length=20)
    renta = models.DecimalField(max_digits=6, decimal_places=2)
    carro = models.ForeignKey(
        Carros, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Rentas"

    def __str__(self):
        return self.nombre


class Pagos(models.Model):

    carro = models.ForeignKey(
        Carros, on_delete=models.CASCADE, blank=False, null=False)
    pago = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    semana = models.CharField(max_length=20)
    startweek = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    endweek = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    renta = models.ForeignKey(
        Renta, on_delete=models.PROTECT, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Pagos"

    def get_absolute_url(self):
        return reverse('pagos')

    def __str__(self):
        return self.semana


class Inactividad(models.Model):
    razon = models.CharField(max_length=20)
    carro = models.ForeignKey(
        Carros, on_delete=models.CASCADE, blank=True, null=True)
    fecha_inicio = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    fecha_fin = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Razon de Inactividad"
