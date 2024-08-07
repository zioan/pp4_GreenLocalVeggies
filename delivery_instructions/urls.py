from django.urls import path
from . import views

urlpatterns = [
    path('', views.instruction_list, name='instruction_list'),
    path('create/', views.instruction_create, name='instruction_create'),
    path('<int:pk>/', views.instruction_detail, name='instruction_detail'),
]
