from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear, name='crear'),
    path('edit/<int:lab_id>/', views.edit, name='edit'),
    path('delete/<int:lab_id>/', views.delete, name='delete'),
]