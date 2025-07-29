from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Product, Client, Contact, Task, Bill, ActiveSubscription

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
	
def ContactAdd(request):

	template = loader.get_template("crm/contactadd.html")
	context = None
	return HttpResponse(template.render(context, request))
	
def ContactSave(request, payload):

	template = loader.get_template("crm/contactsave.html")
	context = {"payload" : payload}
	return HttpResponse(template.render(context, request))
	
def Contacts(request):

	contacts = Contact.objects.all()
	
	template = loader.get_template('crm/contacts.html')
	context = { "contacts" : contacts }
	return HttpResponse(template.render(context, request))
	
def Clients(request):

	clients = Client.objects.all()
	
	template = loader.get_template('crm/clients.html')
	context = { "clients" : clients }
	return HttpResponse(template.render(context, request))
	
def Products(request):

	products = Product.objects.all()
	
	template = loader.get_template('crm/products.html')
	context = { "products" : products }
	return HttpResponse(template.render(context, request))
	
	
def Billing(request):

	try:
		records = Billing.objects.all()
	except AttributeError as e:
		records = []
		
	template = loader.get_template('crm/billing.html')
	context = { 'records' : records }
	return HttpResponse(template.render(context, request))
	
	
def Bills(request):

	records = Bill.objects.all()

	template = loader.get_template('crm/bills.html')
	context = { 'records' : records }
	return HttpResponse(template.render(context, request))
	