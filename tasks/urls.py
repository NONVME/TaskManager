from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_tasks, name='tasks'),
    path('create/', views.task_create, name='task-create'),
    path('<int:pk>/update/', views.task_change, name='task-change'),
    path('<int:pk>/delete/', views.task_delete, name='task-delete'),
]
