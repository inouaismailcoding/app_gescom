from django.db import models
from stock.models import *
# Create your models here.

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    customer=models.CharField("Customer Name",max_length=200,blank=True,null=True)
    customer_number=models.CharField("Customer Number",max_length=20,blank=True,null=True)
    nui=models.CharField("Numero Indentifiant Unique",max_length=40,blank=True,null=True)
    rc=models.CharField("Registre du commerce",max_length=40,blank=True,null=True)
    phone=models.CharField('Numero Telephone',max_length=25,blank=True,null=True)
    mail=models.EmailField('Adresse Email',max_length=200,blank=True,null=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,max_length=20,blank=True,null=True)
    town=models.ForeignKey(Town,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.customer_number
    
class Sale(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    sale_number=models.CharField('reference Vente',max_length=25,blank=True,null=True)
    date=models.DateTimeField(auto_now=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.FloatField('Montal total',blank=True,null=True)
    def __str__(self):
        return self.sale_number
    
class SaleLine(models.Model):
    sale = models.ForeignKey(Sale, related_name='lines', on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE,blank=True,null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2,blank=True,null=True)

    


