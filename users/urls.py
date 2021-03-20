from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('create/', views.user_register, name='user-register'),
    path('<int:pk>/update/', views.user_change, name='user-change'),
    path('<int:pk>/delete/', views.user_delete, name='user-delete'),
]
