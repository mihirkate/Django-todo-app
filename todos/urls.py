from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_word_view, name='hello_world'),
    path('', views.home, name='home'),
    path('hellorender', views.home_render, name='hellorender'),
    path('helloGreetings/<str:name>', views.helloGreetings, name='helloGreetings'),
    path('search', views.search, name='search'),
    path('post_example', views.post_example, name='post_example'),
    path('submitExample', views.submitExample, name='submitExample'),
    path('submitForm', views.submitForm, name='submitForm'),
    path('todos', views.todos_view, name='todos'),
]
