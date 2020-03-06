from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from django.db.models import Sum
from django.db.models.functions import Coalesce
from .models import Conductores, Carros, Polizas, Propietarios, TipoGasto, Renta, Gasto, Pagos
from .serializers import ConductoresSerializer, CarrosSerializer, PolizasSerializer, PropietariosSerializer, TipoGastoSerializer, RentasSerializer
from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView
from .filters import PagosFilter, ConductoresFilter
from .tables import ConductoresTable, PropietariosTable, CarrosTable, PolizasTable, GastosTable, PagosTable, PagosDetailTable
from .forms import PostConductores, EditConductores, PostPropietarios, EditPropietarios, PostCarros, EditCarros, PostPolizas, EditPolizas, PostGasto, EditGasto, PostPagos, EditPagos, AgregarPagoTransaccionExistente
from django.db.models import Sum, Count, Case, When
# Views


def index(request):
    return render(request, 'index.html')


# API views

class ConductoresListView(SingleTableMixin, FilterView):

    table_class = ConductoresTable
    template_name = 'AC/drivers.html'
    filterset_class = ConductoresFilter
    paginate_by = 10


class PropietariosListView(SingleTableView):
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


class GastoListView(SingleTableView):
    model = Gasto
    table_class = GastosTable
    template_name = 'AC/expenses.html'
    paginate_by = 10


class PagosListView(SingleTableMixin, FilterView):
    queryset = Pagos.objects.all().values(
        'carro', 'semana').annotate(PagoTotal=Sum('pago'))
    table_class = PagosTable
    template_name = 'AC/payments.html'
    filterset_class = PagosFilter
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


class GastoCreate(CreateView):
    form_class = PostGasto
    template_name = "AC/add_expense.html"


class GastoUpdate(UpdateView):
    form_class = EditGasto
    model = Gasto
    template_name = "AC/edit_expense.html"


class GastoDelete(DeleteView):
    model = Gasto
    success_url = reverse_lazy('gasto')


class PagosCreate(CreateView):
    form_class = PostPagos
    template_name = "AC/add_payment.html"

    def form_valid(self, form):
        object = form.save(commit=False)
        object.startweek, object.endweek = self.weekdatetimeconverter(
            object.semana)

        self.validation = self.pagos_validation(object.carro_id, object.pago,
                                                object.semana, object.renta_id)
        if self.validation == 1:
            object.save()
        else:
            return self.form_invalid(form)

        return super(PagosCreate, self).form_valid(form)

    def weekdatetimeconverter(self, semana):
        d = semana
        startweek = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
        endweek = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w")
        return (startweek, endweek)

    def pagos_validation(self, carro_id, pago, semana, renta_id):
        intended_payment = pago
        intended_paymentweek = semana
        intended_paymentcar = carro_id
        carrent = renta_id
        fixed_rent = self.get_renta(carrent)
        past_payments = Pagos.objects.filter(
            carro_id=intended_paymentcar, semana=intended_paymentweek).aggregate(total=Coalesce(Sum('pago'), 0))['total']

        if (past_payments + intended_payment) <= fixed_rent:
            validation = 1
            return validation
        else:
            validation = 0
            return validation

    def get_renta(self, carrent):
        rentadecarro = Pagos.objects.select_related('renta').get(id=carrent)
        montoderenta = rentadecarro.renta.renta
        return montoderenta


class PagosDetailView(SingleTableMixin, ListView):

    model = Pagos
    table_class = PagosDetailTable
    template_name = 'AC/paymentsbycarandweek.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        self.object_list = self.object_list.filter(
            carro=kwargs['carro'], semana=kwargs['semana'])

        context = self.get_context_data()
        return self.render_to_response(context)


class AgregarPagoSemana(CreateView):

    template_name = "AC/add_paymentexistingweek.html"
    model = Pagos
    form_class = AgregarPagoTransaccionExistente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'semana': self.kwargs['semana'],
            'carro': self.kwargs['carro'],
        })
        return context

    def get_form_kwargs(self):
        kwargs = super(AgregarPagoSemana, self).get_form_kwargs()
        kwargs['carro'] = self.kwargs.get('carro')
        kwargs['semana'] = self.kwargs.get('semana')
        return kwargs


class PagosUpdate(UpdateView):
    form_class = EditPagos
    model = Pagos
    template_name = "AC/edit_payment.html"

    def form_valid(self, form):
        object = form.save(commit=False)
        object.startweek, object.endweek = self.weekdatetimeconverter(
            object.semana)
        object.save()
        return super(PagosUpdate, self).form_valid(form)

    def weekdatetimeconverter(self, semana):
        d = semana
        startweek = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
        endweek = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w")
        return (startweek, endweek)


class PagosDelete(DeleteView):
    model = Pagos
    success_url = reverse_lazy('pagos')


class HomeView(ListView):
    context_object_name = 'home'
    template_name = 'AC/home.html'
    model = Carros

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['estatusactivos'] = Carros.objects.aggregate(
            activos=Count(Case(When(is_active=True, then=1))))
        context['estatusinactivos'] = Carros.objects.aggregate(
            inactivos=Count(Case(When(is_active=False, then=1))))
        context['totaldecarros'] = Carros.objects.all()
        context['pagos'] = Pagos.objects.all()
        context['Gasots'] = Gasto.objects.all()
        return context
