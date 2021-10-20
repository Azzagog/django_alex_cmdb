from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login_view, name = 'login'),
    path('<str:site_name>/', views.detail, name='detail'),
    path('<str:site_name>/edit', views.edit, name='edit'),
    path('<str:site_name>/contacts', views.contacts, name='contacts'),
    path('<str:site_name>/environment', views.environment, name='environment'),
    path('<str:site_name>/dependent_service', views.dependent_service, name='dependent_service'),
    path('<str:site_name>/environment/<str:environment_description>', views.environment_detail, name='environment_detail'),

]