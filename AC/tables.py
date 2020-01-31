
from django_tables2 import tables, TemplateColumn, LinkColumn
import django_tables2 as tables
from django_tables2.utils import A
from .models import Conductores, Propietarios, Carros, Polizas


class ConductoresTable(tables.Table):

    detalles = TemplateColumn(
        '<a class="btn btn btn-info btn-sm" href="{% url "conductor_edit" record.id %}">Abrir</a>')

    class Meta:
        model = Conductores
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("nombres", "apellidos", "telefono")
        attrs = {"class": "table table-hover table-sm"}


class PropietariosTable(tables.Table):

    detalles = TemplateColumn(
        '<a class="btn btn btn-info btn-sm" href="{% url "propietario_edit" record.id %}">Abrir</a>')

    class Meta:
        model = Propietarios
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("nombres", "apellidos", "telefono")
        attrs = {"class": "table table-hover table-sm"}


class CarrosTable(tables.Table):

    detalles = TemplateColumn(
        '<a class="btn btn btn-info btn-sm" href="{% url "carros_edit" record.id %}">Abrir</a>')

    class Meta:
        model = Carros
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("nombre", "placa", "conductor")
        attrs = {"class": "table table-hover table-sm"}


class PolizasTable(tables.Table):

    detalles = TemplateColumn(
        '<a class="btn btn btn-info btn-sm" href="{% url "poliza_edit" record.id %}">Abrir</a>')

    class Meta:
        model = Polizas
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("nombre", "numero", "carro")
        attrs = {"class": "table table-hover table-sm"}
