from django.urls import path

from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('create/', views.create, name='users-create'),
    path('<int:pk>/update/', views.update, name='users-update'),
    path('<int:pk>/delete/', views.delete, name='users-delete'),
]
