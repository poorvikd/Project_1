from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title,name='title_search'),
    path("search/",views.search_bar,name='search'),
    path("create/",views.create,name='create'),
    url(r"^edit/title-(?P<parameter>[\w-]+)",views.edit, name="edit"),
    path("random/",views.random,name="random")
]
