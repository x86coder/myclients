from django.urls import path

from . import views


urlpatterns = [
	path("", views.index, name="index"),
	path("tasks", views.Tasks, name="tasks"),
	path("tasks/<int:task_id>", views.TaskDetail, name="taskdetail"),
	path("contacts/add", views.ContactAdd),
	path("contacts", views.Contacts),
]