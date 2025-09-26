# core/filters.py
import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    job_type = django_filters.CharFilter(field_name='job_type', lookup_expr='exact')
    category = django_filters.NumberFilter(field_name='category__id', lookup_expr='exact')

    class Meta:
        model = Job
        fields = ['title', 'location', 'job_type', 'category']
