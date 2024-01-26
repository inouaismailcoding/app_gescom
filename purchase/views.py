from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import  *
from stock.models import Category,Article,Package
from stock.functions import *
from .forms import *
# Create your views here.


def list_supplier(request):
    context={}
    context['suppliers']=Supplier.objects.all().order_by("supplier")
    if 'format' in request.GET :
       return get_data_table_file(request,Supplier)
    return render(request,'list_supplier.html',context)
    

def add_supplier(request):
    context={}
    context['form']=SupplierForm()
    if request.method =="POST":
        
        form=SupplierForm(request.POST)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.supplier_number=genererRef(Supplier,'SUP')
            instance.save()
            messages.success(request,"le fournisseur a été enregistré avec success")
            return redirect('list_supplier')
        else: return render(request,'add_supplier.html',{'errors':form.errors,'form':form})
          
    else :
        form=SupplierForm()
        context['form']=form
        return render(request,'add_supplier.html',context)
    
def edit_supplier(request,id):
    context={}
    instance=get_object_or_404(Supplier,id=id)
    context['instance']=instance
    if request.method == "POST":
        form=SupplierForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'edit successfuly !')
            return redirect('list_supplier')
        else:
            return render(request,'edit_supplier.html',context)
    else: 
        form=SupplierForm(instance=instance)
        context['form']=form        
        return render(request,"edit_supplier.html",context)

# procedure pour Supprimer un Fournisseur
def delete_supplier(request,id):
    if request.method =='POST':
        row=Supplier.objects.get(id=id)
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_supplier')
    else:
        context={}
        context['supplier']=Supplier.objects.get(id=id)
        context['articles']=Article.objects.filter(category=id)
        return render(request,'delete_supplier.html',context)

def info_supplier(request,id):
    context={}
    context['supplier']=Supplier.objects.get(id=id)
    return render(request,'info_supplier.html',context)


def list_purchase(request):
    context={}
    context['purchases']=Purchase.objects.all().order_by("date")
    if 'format' in request.GET :
       return get_data_table_file(request,Purchase)
    return render(request,'list_purchase.html',context)


def add_purchase(request):
    context={}
    context['categorys']=Category.objects.all().order_by('category')
    purchaseForm=PurchaseForm()
    if request.method=='POST':
        # On cree d'abord la facture
        amount=request.POST.get('amount')
        supplier=request.POST.get('supplier')
        supplier=Supplier.objects.get(id=supplier)
        purchase_number=genererRef(Purchase,'PUR.000')
        instance=purchaseForm.save(commit=False)
        instance.amount=amount
        instance.supplier=supplier
        instance.purchase_number=purchase_number
        instance.user=request.user
        instance.save()
        line_data = request.POST.getlist('lines[]')
        line_data=saveRow(line_data)
        for line in line_data:
            form = PurchaseLineForm(line)
            if form.is_valid():
                line_instance = form.save(commit=False)
                line_instance.purchase = instance
                line_instance.save()  
        messages.success(request,"L'achat a été enregistré avec success")
        return redirect("list_purchase")
        # On enregistre les differents lignes de facture
    elif  request.method=='GET':
        if 'fetchAll' in request.GET:
            data={}
            data['category']=list(Category.objects.all().values())
            data['article']=list(Article.objects.all().values())
            data['package']=list(Package.objects.all().values())
            return JsonResponse(data)
    context['purchaseForm']=purchaseForm
    return render(request,'add_purchase.html',context)


def info_purchase(request,id):
    context={}
    context['purchase']=Purchase.objects.get(id=id)
    context['purchaseline']=PurchaseLine.objects.filter(purchase=id)


    return render(request,'info_purchase.html',context)


def delete_purchase(request,id):
    context={}
    if request.method =='POST':
        row=Purchase.objects.get(id=id)
        detail=PurchaseLine.objects.filter(purchase=id)
        detail.delete()
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_purchase')

    else:
        context['purchase']=Purchase.objects.get(id=id)
        context['purchaseline']=PurchaseLine.objects.filter(purchase=id)
    return render(request,'delete_purchase.html',context)

