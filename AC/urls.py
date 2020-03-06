from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django_filters.views import FilterView
from .filters import PagosFilter
from .models import Pagos, Conductores

from . import filters

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('conductores_list/', views.conductores),
    path('drivers/', views.ConductoresListView.as_view(model=Conductores),
         name='conductores'),
    path('drivers/add/', views.ConductoresCreate.as_view(), name='conductor_new'),
    path('drivers/<int:pk>/',
         views.ConductoresUpdate.as_view(), name='conductor_edit'),
    path('drivers/<int:pk>/borrar/',
         views.ConductoresDelete.as_view(), name='conductor_borrar'),
    path('owners/', views.PropietariosListView.as_view(), name='propietarios'),
    path('owners/add/', views.PropietariosCreate.as_view(), name='propietario_new'),
    path('owners/<int:pk>/',
         views.PropietariosUpdate.as_view(), name='propietario_edit'),
    path('owners/<int:pk>/borrar/',
         views.PropietariosDelete.as_view(), name='propietario_borrar'),
    path('cars/', views.CarrosListView.as_view(), name='carros'),
    path('cars/add/', views.CarrosCreate.as_view(), name='carros_new'),
    path('cars/<int:pk>/',
         views.CarrosUpdate.as_view(), name='carros_edit'),
    path('cars/<int:pk>/borrar/',
         views.PropietariosDelete.as_view(), name='carros_borrar'),

    path('insurance/', views.PolizasListView.as_view(), name='polizas'),
    path('insurance/add/', views.PolizaCreate.as_view(), name='poliza_new'),
    path('insurance/<int:pk>/',
         views.PolizaUpdate.as_view(), name='poliza_edit'),
    path('insurance/<int:pk>/borrar/',
         views.PolizaDelete.as_view(), name='poliza_borrar'),

    path('expenses/', views.GastoListView.as_view(), name='gasto'),
    path('expenses/add/', views.GastoCreate.as_view(), name='gasto_new'),
    path('expenses/<int:pk>/',
         views.GastoUpdate.as_view(), name='gasto_edit'),
    path('expenses/<int:pk>/borrar/',
         views.GastoDelete.as_view(), name='gasto_borrar'),

    path('payments/', views.PagosListView.as_view(model=Pagos), name='pagos'),
    path('payments/addtoexistingweek/<int:carro>/<slug:semana>',
         views.AgregarPagoSemana.as_view(), name='pago_existente'),
    path('payments/add/', views.PagosCreate.as_view(), name='pagos_new'),
    path('paymentsbycarandweek/<int:carro>/<slug:semana>',
         views.PagosDetailView.as_view(), name='pagos_bycar'),
    path('payments/<int:pk>/borrar/',
         views.PagosDelete.as_view(), name='pagos_borrar'),

    path('api/conductores', views.ListaConductores.as_view()),
    path('api/carros', views.ListaCarros.as_view()),
    path('api/polizas', views.ListaPolizas.as_view()),
    path('api/propietarios', views.ListaPropietarios.as_view()),
    path('api/tipogasto', views.ListaTipoGasto.as_view()),
    path('api/renta', views.ListaRentas.as_view()),
    path('api/conductores/<int:pk>/', views.DetalleConductores.as_view()),
    path('api/carros/<int:pk>/', views.DetalleCarros.as_view()),
    path('api/polizas/<int:pk>/', views.DetallePolizas.as_view()),
    path('api/propietarios/<int:pk>/', views.DetallePropietarios.as_view()),
    path('api/tipogasto/<int:pk>/', views.DetalleTipoGasto.as_view()),
    path('api/renta/<int:pk>/', views.DetalleRentas.as_view())

]
