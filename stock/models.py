from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category = models.CharField('categorie',max_length=150, blank=True, null=True)
    image=models.ImageField(upload_to='image_category',blank=True,null=True)
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.category
    
class Package(models.Model): 
    package = models.CharField('emballage',max_length=10, blank=True, null=True)
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return  self.package
    
class Article(models.Model):
    category=models.ForeignKey(Category,blank=True,null=True, on_delete=models.CASCADE)
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    img_article=models.ImageField(upload_to='image_category',blank=True,null=True)
    article_number=models.CharField('reference article',max_length=200, blank=True, null=True)
    article=models.CharField('Article',max_length=200, blank=True, null=True)
    package=models.ForeignKey(Package,blank=True,null=True, on_delete=models.CASCADE)
    price=models.FloatField('Prix unitaire',blank=True,null=True)

    def __str__(self):
        return self.article_number

class Country(models.Model):
    country = models.CharField('Pays',max_length=150, blank=True, null=True)
    def __str__(self):
        return self.country


class Town(models.Model):
    country=models.ForeignKey(Country,blank=True,null=True, on_delete=models.CASCADE)
    town=models.CharField('Ville',max_length=200, blank=True, null=True)