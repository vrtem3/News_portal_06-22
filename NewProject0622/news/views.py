from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Category, Post, PostCategory, Comment
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_create'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'blog.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'postlist'
    paginate_by = 5 # вот так мы можем указать количество записей на странице

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

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
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    ordering = 'post_title'
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


#def post_create(request):
#    form = PostForm()
#    
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/blog/')
#    
#    return render(request, 'post_form.html', {'form': form})

# Добавляем представление для создания нового объекта
class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_form.html'


# Добавляем представление для изменения товара.
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_form.html'


# Представление удаляющее товар.
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')