import django_filters
from .models import Etudiant
class EtudiantFilter(django_filters.FilterSet):
    mat = django_filters.CharFilter(field_name='mat',lookup_expr='icontains')
    nom = django_filters.CharFilter(field_name='nom',lookup_expr='icontains')
    prenom = django_filters.CharFilter(field_name='prenom',lookup_expr='icontains')
    year = django_filters.NumberFilter(field_name='date_de_naissance',lookup_expr='year')
    month = django_filters.NumberFilter(field_name='date_de_naissance',lookup_expr='month')
    day = django_filters.NumberFilter(field_name='date_de_naissance',lookup_expr='day')


    class Meta:
        model = Etudiant
        fields = '__all__'