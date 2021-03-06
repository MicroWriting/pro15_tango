from django.urls import path
from . import views


app_name ='app'

urlpatterns= [
    path('', views.IndexView.as_view(), name='index'),
    path('tag/<str:tag>/', views.TagView.as_view(), name='tag'),
    path('sort/', views.sort, name='sort')
]
