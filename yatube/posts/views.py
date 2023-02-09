from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница сайта Yatube'
    context = {
        'posts': posts,
        'title': title
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title': 'Страница группы',
        'text': 'Лев Толстой – зеркало русской революции.'
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
