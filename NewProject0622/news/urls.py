from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, post_create


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
    path('', PostList.as_view()), 
    path('<int:post_id>', PostDetail.as_view()),
    path('create/', post_create, name='post_create')
]