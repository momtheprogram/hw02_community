from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:10]
    title = 'Главная страница сайта Yatube'
    context = {
        'posts': posts,
        'title': title
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
