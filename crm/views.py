from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Product, Client

def index(request):

    records = Product.objects.all()
    
    template = loader.get_template("crm/index.html")
    context = {"records" : records}
    res = HttpResponse(template.render(context, request))
    
    return res