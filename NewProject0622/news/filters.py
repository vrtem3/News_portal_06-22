from django_filters import FilterSet, DateFilter
from .models import Post
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    date_create = DateFilter(field_name='date_create',
                      lookup_expr='gte',
                      label='Создан позднее',
                      widget=DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ['post_title', 'date_create', 'category_type']
