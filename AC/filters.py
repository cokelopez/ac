
import django_filters
from .models import Pagos
from .tables import PagosTable


class PagosFilter(django_filters.FilterSet):
    semana = django_filters.ModelChoiceFilter(field_name='semana',
                                              queryset=Pagos.objects.order_by('semana').distinct('semana'))

    class Meta:
        model = Pagos
        fields = ['semana', ]
