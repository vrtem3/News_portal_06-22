from django_filters import FilterSet, ModelChoiceFilter, DateFilter, CharFilter
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ['post_title', 'date_create', 'category_type']












#  Старый код, написал заново фильтры.

#class PostFilter(FilterSet):
# ModelChoiceFilter работает со связанными моделями, используемыми ForeignKeyпо умолчанию.
#    Post = ModelChoiceFilter(
#        field_name='category_type',
#        queryset=Post.objects.all(),
#        label='Категория'
#    )

#    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
#       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
#       fields = {
           # поиск по названию
#           'post_title': ['icontains'],
           # количество товаров должно быть больше или равно
#           'date_create': ['gt'],
#        }

#    date_create = DateFilter(field_name='date_create',
#                             lookup_expr='gte',
#                             label='Дата создания',
#                             widget=forms.DateInput(attrs={'type': 'date'}))
#    post_title = CharFilter(lookup_expr='icontains')
#    post_title = forms.CharFilter(lookup_expr='icontains',
#                                 label='Укажите название')
#    post_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search'}))
#
#    class Meta:
#        model = Post
#        fields = ['post_title', 'date_create']



#class PostFilter(FilterSet):
#    date = DateFilter(field_name='dateCreation',
#                      lookup_expr='gte',
#                      label='Create after',
#                      widget=DateInput(attrs={'type': 'date'}))
#    title = CharFilter(lookup_expr='icontains')
#    author = ModelChoiceFilter(queryset=Author.objects.all())
#    date.field.error_messages = {'invalid': 'Enter date in format DD.MM.YYYY. Example: 31.12.2020'}
#    date.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}
#
#    class Meta:
#        model = Post
#        fields = ['date', 'title', 'author']



#class Post_Filter(forms.Form):
#    date_create = DateFilter(field_name='date_create',
#                             lookup_expr='gte',
#                             label='Дата создания',
#                             widget=forms.DateInput(attrs={'type': 'date'}))
#    post_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search'}))
#
#    class Meta:
#        model = Post
#        fields = ['post_title', 'date_create']