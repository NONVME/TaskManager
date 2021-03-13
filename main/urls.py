from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tasks', views.tasks, name='tasks'),
    path('about2', views.about2, name='about2'),
]
