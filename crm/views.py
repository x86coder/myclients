from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Product, Client, Contact, Task

def index(request):
	contacts = Contact.objects.all()
	tasks = Task.objects.all()
	
	template = loader.get_template("crm/index.html")
	context = {"records" : contacts, "tasks" : tasks}
	res = HttpResponse(template.render(context, request))
	
	return res
	
def Tasks(request):

	tasks = Task.objects.all()
	
	template = loader.get_template('crm/tasks.html')
	context = { "tasks" : tasks }
	return HttpResponse(template.render(context, request))
	
def TaskDetail(request, task_id):
	task = Task.objects.get(pk=task_id)
	
	template = loader.get_template("crm/taskdetail.html")
	context = {"task" : task}
	return HttpResponse(template.render(context, request))
	
def TaskAdd(request):

	template = loader.get_template("crm/taskadd.html")
	context = {"data" : None}
	return HttpResponse(template.render(context, request))
	
def Contacts(request):

	contacts = Contact.objects.all()
	
	template = loader.get_template('crm/contacts.html')
	context = { "contacts" : contacts }
	return HttpResponse(template.render(context, request))