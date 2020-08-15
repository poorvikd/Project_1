from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title,name='title_search'),
    path("search/",views.search_bar,name='search'),
    path("create/",views.create,name='create')
]
