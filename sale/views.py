from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from .forms import *
from stock.functions import *
# Create your views here.


def list_customer(request):
    context={}
    context['customers']=Customer.objects.all().order_by('customer')
    if 'format' in request.GET :
       return get_data_table_file(request,Customer)
    return render(request,'list_customer.html',context)

def add_customer(request):
    context={}
    if request.method =="POST":    
        form=CustomerForm(request.POST)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.customer_number=genererRef(Customer,'CUS')
            instance.save()
            messages.success(request,"le Client a été enregistré avec success")
            return redirect('list_customer')
        else: return render(request,'add_customer.html',{'errors':form.errors,'form':form})
          
    else :
        form=CustomerForm()
        context['form']=form
        return render(request,'add_customer.html',context)

def edit_customer(request,id):
    context={}
    instance=get_object_or_404(Customer,id=id)
    context['instance']=instance
    if request.method == "POST":
        form=CustomerForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'edit successfuly !')
            return redirect('list_customer')
        else:
            return render(request,'edit_customer.html',context)
    else: 
        form=CustomerForm(instance=instance)
        context['form']=form        
        return render(request,"edit_customer.html",context)

def delete_customer(request,id):
    if request.method =='POST':
        row=Customer.objects.get(id=id)
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_customer')
    else:
        context={}
        context['customer']=Customer.objects.get(id=id)
        context['sales']=Sale.objects.filter(customer=id)
        return render(request,'delete_customer.html',context)

def info_customer(request,id):
    context={}
    context['customer']=Customer.objects.get(id=id)
    context['sales']=Sale.objects.filter(customer=id)
    return render(request,'info_customer.html',context)

def list_sale(request):
    context={}
    context['sales']=Sale.objects.all().order_by("date")
    if 'format' in request.GET :
       return get_data_table_file(request,Article)

    return render(request,'list_sale.html',context)

def add_sale(request):
    context={}
    context['categorys']=Category.objects.all().order_by('category')
    saleForm=SaleForm()
    if request.method=='POST':
        # On cree d'abord la facture
        amount=request.POST.get('amount')
        customer=request.POST.get('customer')
        customer=Customer.objects.get(id=customer)
        sale_number=genererRef(Sale,'SAL')
        instance=saleForm.save(commit=False)
        instance.amount=amount
        instance.customer=customer
        instance.sale_number=sale_number
        instance.user=request.user
        instance.save()
        line_data = request.POST.getlist('lines[]')
        line_data=saveRow(line_data)
        for line in line_data:
            form = SaleLineForm(line)
            if form.is_valid():
                line_instance = form.save(commit=False)
                line_instance.sale = instance
                line_instance.save()  
        messages.success(request,"La facture de Vente a été enregistré avec success")
        return redirect("list_sale")
        # On enregistre les differents lignes de facture
    elif  request.method=='GET':
        if 'fetchAll' in request.GET:
            data={}
            data['category']=list(Category.objects.all().values())
            data['article']=list(Article.objects.all().values())
            data['package']=list(Package.objects.all().values())
            return JsonResponse(data)
    context['purchaseForm']=SaleForm
    return render(request,'add_sale.html',context)


def info_sale(request,id):
    context={}
    context['sale']=Sale.objects.get(id=id)
    context['saleLine']=SaleLine.objects.filter(sale=id)
    if 'format' in request.GET :
       return get_data_table_file(request,Sale)

    return render(request,'info_sale.html',context)


def delete_sale(request,id):
    context={}
    if request.method =='POST':
        row=Sale.objects.get(id=id)
        detail=Sale.objects.filter(sale=id)
        detail.delete()
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_sale')

    else:
        context['sale']=Sale.objects.get(id=id)
        context['saleLine']=SaleLine.objects.filter(sale=id)
    return render(request,'delete_sale.html',context)

