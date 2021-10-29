from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications/', views.applications, name='applications'),
    path('environments/', views.environments, name='environments'), 
    path('servers/', views.servers, name='servers'),
    path('contacts/', views.contacts, name='contacts'),
    path('credentials/', views.credentials, name='credentials'),
    path('<str:site_name>/', views.detail, name='detail'),
    path('<str:site_name>/edit', views.edit, name='edit'),        
    path('<str:site_name>/dependent_service', views.dependent_service, name='dependent_service'),
    path('<str:site_name>/environments/<str:environment_description>', views.environment_detail, name='environment_detail'),    
    path('<str:site_name>/environments/<str:environment_description>/<str:application_name>/', views.applications_detail, name='applications_detail'),

]