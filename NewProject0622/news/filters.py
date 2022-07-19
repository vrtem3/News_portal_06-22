from django_filters import FilterSet, ModelChoiceFilter
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    Post = ModelChoiceFilter(
        field_name='category_type',
        queryset=Post.objects.all(),
        label='Категория'
    )

    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'post_title': ['icontains'],
           # количество товаров должно быть больше или равно
           'date_create': ['gte'],
        }
