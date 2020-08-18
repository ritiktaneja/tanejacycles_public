from rest_framework import generics
import django_filters
from django_filters import rest_framework as filters
from distutils.util import strtobool

from .models import Bicycle
from .constants import Speed,Size

class BicycleFilter(filters.FilterSet):

    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price',lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price',lookup_expr='lt')
    brand__name = django_filters.CharFilter(lookup_expr='icontains')
    wheel_size = django_filters.MultipleChoiceFilter(choices=[(i.name,i.value) for i in Size])
    category = django_filters.CharFilter(lookup_expr='icontains')
    speed = django_filters.MultipleChoiceFilter(choices=[(i.name,i.value) for i in Speed])
    featured = django_filters.BooleanFilter()
    in_stock = django_filters.BooleanFilter()
    on_sale = django_filters.BooleanFilter()

    class Meta:
        model = Bicycle
        fields = {
            'price': ['lt', 'gt'],
            
        }
       