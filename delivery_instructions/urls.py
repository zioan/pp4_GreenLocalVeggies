from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.instruction_create, name='instruction_create'),
    path('<int:pk>/update/', views.instruction_update,
         name='instruction_update'
         ),
    path('<int:pk>/delete/', views.instruction_delete,
         name='instruction_delete'
         ),
    path('<int:pk>/', views.instruction_detail, name='instruction_detail'),
]
