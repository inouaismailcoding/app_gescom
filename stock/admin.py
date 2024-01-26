from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Article) # Model Article
admin.site.register(models.Category) # Model Category
admin.site.register(models.Package) # Model Package
admin.site.register(models.Country) # Model Country
admin.site.register(models.Town) # Model Town
