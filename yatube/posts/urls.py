from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница с постами выбраной группы
    path('group/<slug>/', views.group_posts, name='group_list'),
]
