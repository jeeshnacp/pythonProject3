from django import forms
from django_filters import CharFilter
import django_filters

from app.models import hospital


class HospitalFilter(django_filters.FilterSet):
    name = CharFilter(field_name='place', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Place', 'class': 'form-control'}))

    class Meta:
        model = hospital
        fields = ['name']
