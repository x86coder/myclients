from django.db import models

class Client(models.Model):
    company = models.CharField(max_length=160, blank=False, null=False)
    date_added = models.DateField(auto_now_add = True)
    #payment_method
    def __str__(self):
        return self.company
    
class Contact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=160, blank=True, null=True)
    position = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    notes = models.TextField()
    
    def __str__(self):
        return self.name
        
# class Employee(models.Model):

class Product(models.Model):
    name = models.CharField(max_length=160, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    #Owner
    #Dept.
    #Category

    def __str__(self):
        return self.name
        
class Billing(models.Model):
    type_txt = models.CharField(max_length=64)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    period_days = models.IntegerField(default=30, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    tax = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    
    def __str__(self):
        return self.type_txt
    
class Bill(models.Model):
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    tax = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    #payment_method
    
class ActiveSubscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)
    
class Task(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False)
    notes = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=False, null=False)
    due_date = models.DateTimeField(blank=False, null=False)
    
    def __str__(self):
        return self.name
