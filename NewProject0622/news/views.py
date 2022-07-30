from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-date_create' # сортируем по дате объекты
    template_name = 'blog.html' # указываем шаблон, в котором выводим объекты
    context_object_name = 'postlist' # имя списка объектов, к которому обращаемся в html-шаблоне
    paginate_by = 5 # указываем, сколько выводить объектов на странице

    def get_queryset(self):
        queryset = super().get_queryset() # Получаем обычный запрос, используем наш класс фильтрации
        self.filterset = PostFilter(self.request.GET, queryset) # self.request.GET содержит объект QueryDict, сохраняем нашу фильтрацию в объекте класса
        # чтобы потом добавить в контекст и использовать в шаблоне.
        return self.filterset.qs # Возвращаем из функции отфильтрованный список товаров

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    ordering = 'post_title'
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


# Представление для создания нового объекта
class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_form.html'


# Представление для изменения объекта
class PostEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_form.html'


# Представление для удаления товара
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')