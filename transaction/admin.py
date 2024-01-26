from django.contrib import admin
from .models import Mouvement,Transaction,Intervenant,TransactionLine
# Register your models here.
admin.site.register(Mouvement)
admin.site.register(Transaction)
admin.site.register(TransactionLine)
admin.site.register(Intervenant)