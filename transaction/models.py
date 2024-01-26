from django.db import models
from django.contrib.auth.models import User
from stock.models import Country,Town,Article

# Create your models here.

class Intervenant(models.Model):
    DEPARTMENT=(('account','account'),('Marketing','Marketing'),('Administration','Administration'),('Technical','Technical'),)
    DIRECTION=(('Agency','Agency'),('HQ','Head Quarter'),)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    intervenant=models.CharField("Intervenant Name",max_length=200,blank=True,null=True)
    intervenant_number=models.CharField("Customer Number",max_length=20,blank=True,null=True)
    matricule=models.CharField("Matricule",max_length=40,blank=True,null=True)
    post_occuped=models.CharField("Poste Occupé",max_length=150,blank=True,null=True)
    direction=models.CharField("direction",choices=DIRECTION,max_length=20,blank=True,null=True)
    dept=models.CharField("department",choices=DEPARTMENT,max_length=20,blank=True,null=True)
    
    phone=models.CharField('Numero Telephone',max_length=25,blank=True,null=True)
    mail=models.EmailField('Adresse Email',max_length=200,blank=True,null=True)
    town=models.ForeignKey(Town,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.intervenant_number


class Mouvement(models.Model):
    MOUVEMENT=(('IN','IN'),('OUT','OUT'))
    mouvement=models.CharField('Mouvement',choices=MOUVEMENT,max_length=20,blank=True,null=True)
    def __str__(self):
        return self.mouvement
    
class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    transaction_number=models.CharField('reference transaction',max_length=25,blank=True,null=True)
    date=models.DateTimeField(auto_now=True)
    intervenant=models.ForeignKey(Intervenant,on_delete=models.CASCADE,blank=True,null=True)
    mouvement=models.ForeignKey(Mouvement,on_delete=models.CASCADE,blank=True,null=True)
    full_quantity=models.FloatField('Montal total',blank=True,null=True)
    def __str__(self):
        return self.transaction_number
    

class TransactionLine(models.Model):
    transaction = models.ForeignKey(Transaction, related_name='lines', on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    

    

