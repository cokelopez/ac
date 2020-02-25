from django.contrib import admin
from .models import Conductores, Carros, Polizas, Propietarios, TipoGasto, Gasto, Renta, Pagos

admin.site.register(Carros)

admin.site.register(Polizas)
admin.site.register(Propietarios)
admin.site.register(TipoGasto)
admin.site.register(Pagos)


admin.site.site_header = "Administracion de Vehículos"


class GastoAdmin(admin.ModelAdmin):
    list_display = ('carro', 'gasto', 'fecha', 'monto')
    list_filter = ('carro',)


admin.site.register(Gasto, GastoAdmin)


class RentaAdmin(admin.ModelAdmin):
    list_display = ('carro', 'renta')
    list_filter = ('carro',)


admin.site.register(Renta, RentaAdmin)


class ConductoresAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'telefono')


admin.site.register(Conductores, ConductoresAdmin)
