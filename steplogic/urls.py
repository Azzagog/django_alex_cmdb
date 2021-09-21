from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:site_name>/', views.detail, name='detail'),
    path('<str:site_name>/edit', views.edit, name='detail'),

]