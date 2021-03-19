from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('create/', views.register, name='users-register'),
    path('<int:pk>/update/', views.update, name='users-update'),
    path('<int:pk>/delete/', views.delete, name='users-delete'),
]
