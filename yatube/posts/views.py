from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


# Главная страница
def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница сайта Yatube'
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': title
    }
    template = 'posts/index.html'
    return render(request, template, context) 


# Страница c постами, отфильтрованными по группам.
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': 'Страница группы',
        'text': 'Лев Толстой – зеркало русской революции.'
    }
    template = 'posts/group_list.html'
    return render(request, template, context)










    # Cтарый код
    # template_group = 'posts/group_list.html'
    # title_group = 'Здесь будет информация о группах проекта Yatube'
    # text_group = 'Лев Толстой – зеркало русской революции.'
    # context_group = {
    #     'title': title_group,
    #     'text': text_group
    # }
    # return render(request, template_group, context_group)



# Код не пригодился
# Страница с полным текстом поста;
# view-функция принимает параметр pk из path()
#def posts_detail(request, pk):
#   return HttpResponse(f'Полный текст поста {pk}') 
