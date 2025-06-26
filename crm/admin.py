from django.contrib import admin

# Register your models here.
from .models import Task, ActiveSubscription, Bill, Billing, Product, Contact, Client

admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Billing)
admin.site.register(Bill)
admin.site.register(ActiveSubscription)
admin.site.register(Task)