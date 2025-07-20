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