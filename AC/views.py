from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Conductores, Carros, Polizas, Propietarios, TipoGasto, Renta
from .serializers import ConductoresSerializer, CarrosSerializer, PolizasSerializer, PropietariosSerializer, TipoGastoSerializer, RentasSerializer
from django_tables2 import SingleTableView
from .tables import ConductoresTable, PropietariosTable, CarrosTable, PolizasTable
from .forms import PostConductores, EditConductores, PostPropietarios, EditPropietarios, PostCarros, EditCarros, PostPolizas, EditPolizas
# Views


def index(request):
    return render(request, 'index.html')


# API views

class ConductoresListView(SingleTableView):
    model = Conductores
    table_class = ConductoresTable
    template_name = 'AC/drivers.html'
    paginate_by = 10


class ConductoresListView(SingleTableView):
    model = Propietarios
    table_class = PropietariosTable
    template_name = 'AC/propietarios.html'
    paginate_by = 10


class CarrosListView(SingleTableView):
    model = Carros
    table_class = CarrosTable
    template_name = 'AC/carros.html'
    paginate_by = 10


class PolizasListView(SingleTableView):
    model = Polizas
    table_class = PolizasTable
    template_name = 'AC/insurance.html'
    paginate_by = 10


class ListaConductores(generics.ListCreateAPIView):
    queryset = Conductores.objects.all()
    serializer_class = ConductoresSerializer


class DetalleConductores(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conductores.objects.all()
    serializer_class = ConductoresSerializer


class ListaCarros(generics.ListCreateAPIView):
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer


class DetalleCarros(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer


class ListaPolizas(generics.ListCreateAPIView):
    queryset = Polizas.objects.all()
    serializer_class = PolizasSerializer


class DetallePolizas(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polizas.objects.all()
    serializer_class = PolizasSerializer


class ListaPropietarios(generics.ListCreateAPIView):
    queryset = Propietarios.objects.all()
    serializer_class = PropietariosSerializer


class DetallePropietarios(generics.RetrieveUpdateDestroyAPIView):
    queryset = Propietarios.objects.all()
    serializer_class = PropietariosSerializer


class ListaTipoGasto(generics.ListCreateAPIView):
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer


class DetalleTipoGasto(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer


class ListaRentas(generics.ListCreateAPIView):
    queryset = Renta.objects.all()
    serializer_class = RentasSerializer


class DetalleRentas(generics.RetrieveUpdateDestroyAPIView):
    queryset = Renta.objects.all()
    serializer_class = RentasSerializer


# class conductores(ListView):
#     model = conductores
#     paginate_by = 10


# class conductores_sort(ListView):
#     model = conductores
#     paginate_by = 10

#     def get_queryset(self):
#         queryset = super(conductores_sort, self).get_queryset()
#         if self.kwargs.get('sort'):
#             sort_by = self.kwargs.get('sort')
#             if sort_by == 'nombres':
#                 sort_by = '-nombres'
#             elif sort_by == "-nombres":
#                 sort_by = 'nombres'
#             else:
#                 sort_by = 'nombres'
#             return queryset.order_by(sort_by)
#         return queryset

def conductores(request):
    return render(request, 'AC/conductores_list.html')


class ConductoresCreate(CreateView):
    form_class = PostConductores
    template_name = "AC/add_driver.html"


class ConductoresUpdate(UpdateView):
    form_class = EditConductores
    model = Conductores
    template_name = "AC/edit_driver.html"


class ConductoresDelete(DeleteView):
    model = Conductores
    success_url = reverse_lazy('conductores')


class PropietariosCreate(CreateView):
    form_class = PostPropietarios
    template_name = "AC/add_owner.html"


class PropietariosUpdate(UpdateView):
    form_class = EditPropietarios
    model = Propietarios
    template_name = "AC/edit_owner.html"


class PropietariosDelete(DeleteView):
    model = Propietarios
    success_url = reverse_lazy('propietarios')


class CarrosCreate(CreateView):
    form_class = PostCarros
    template_name = "AC/add_car.html"


class CarrosUpdate(UpdateView):
    form_class = EditCarros
    model = Carros
    template_name = "AC/edit_car.html"


class CarrosDelete(DeleteView):
    model = Carros
    success_url = reverse_lazy('carros')


class PolizaCreate(CreateView):
    form_class = PostPolizas
    template_name = "AC/add_insurance.html"


class PolizaUpdate(UpdateView):
    form_class = EditPolizas
    model = Polizas
    template_name = "AC/edit_insurance.html"


class PolizaDelete(DeleteView):
    model = Polizas
    success_url = reverse_lazy('polizas')
