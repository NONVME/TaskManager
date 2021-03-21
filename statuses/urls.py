from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_statuses, name='statuses'),
    path('create/', views.status_create, name='status-create'),
    path('<int:pk>/update/', views.status_change, name='status-change'),
    path('<int:pk>/delete/', views.status_delete, name='status-delete'),
]
