from django.urls import path

from . import views


urlpatterns = [
	path("", views.index, name="index"),
	path("tasks/<int:task_id>", views.TaskDetail, name="tasks"),
	path("tasks/add", views.TaskAdd, name="taskadd"),
]