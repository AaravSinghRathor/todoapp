from django.urls import path

from . import views
from .views import (
    TaskListView,
    TaskDetailedView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView, 
    UserTaskListView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="blog-home"),
    path("user/<str:username>", UserTaskListView.as_view(), name="user-tasks"),
    path("task/<int:pk>/", TaskDetailedView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("about/", views.about, name="blog-about"),
]
