from django.urls import path
from .views import create_task, get_tasks, update_task

urlpatterns = [
    path('create/', create_task),
    path('tasks/', get_tasks),
    path('update/', update_task),
]