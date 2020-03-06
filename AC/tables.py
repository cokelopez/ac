import os
from django_tables2 import tables, TemplateColumn, LinkColumn
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
import django_tables2 as tables
from django_tables2.utils import A
from .models import Conductores, Propietarios, Carros, Polizas, Gasto, Renta, Pagos
from django.utils.html import format_html


class PropietariosTable(tables.Table):

    detalles = TemplateColumn(
        '<a class="btn btn btn-info btn-sm" href="{% url "propietario_edit" record.id %}">Abrir</a>')

    class Meta:
        model = Propietarios
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("nombres", "apellidos", "telefono")
        attrs = {"class": "table table-hover table-sm"}


class CarrosTable(tables.Table):

    class Meta:
        model = Carros
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("nombre", "placa", "conductor")
        attrs = {"class": "table table-hover table-sm"}


class GastosTable(tables.Table):

    detalles = TemplateColumn(
        '<a class="btn btn btn-info btn-sm" href="{% url "gasto_edit" record.id %}">Editar</a>')

    class Meta:
        model = Gasto
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ('monto', 'iva', 'fecha', 'gasto', 'carro', 'factura')
        attrs = {"class": "table table-hover table-sm"}


class PagosTable(tables.Table):

    detalles = TemplateColumn(
        '<a class="btn btn btn-info btn-sm" href="{% url "pagos_bycar" carro=record.carro semana=record.semana %}">Abrir</a>')

    class Meta:
        model = Pagos
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ('carro', 'semana', 'PagoTotal')
        attrs = {"class": "table table-hover table-sm"}


class ImageColumn(tables.Column):

    def render(self, value):
        return format_html('<a href="/media/{0}" download>{0}</a>', value)


class PagosDetailTable(tables.Table):
    imagen = ImageColumn()

    class Meta:
        model = Pagos
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ('carro', 'semana', 'fecha', 'pago')
        attrs = {"class": "table table-hover table-sm"}


class ConductoresTable(tables.Table):

    ine = ImageColumn()

    class Meta:
        model = Conductores
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ('nombres', 'apellidos', 'telefono', 'edad')
        attrs = {"class": "table table-hover table-sm"}


class PolizasTable(tables.Table):

    class Meta:
        model = Polizas
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("nombre", "numero", 'aseguradora', "carro", 'documento')
        attrs = {"class": "table table-hover table-sm"}
