from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .forms import *
from stock.models import *
from stock.functions import *
from stock.reports import *

# Create your views here.

def list_intervenant(request):
    context={}
    context['intervenants']=Intervenant.objects.all()
    if 'format' in request.GET :
       return get_data_table_file(request,Intervenant)
    return render(request,'list_intervenant.html',context)

def add_intervenant(request):
    context={}
    if request.method =="POST":    
        form=IntervenantForm(request.POST)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.intervenant_number=genererRef(Intervenant,'INT')
            instance.save()
            messages.success(request,"l'intervenant a été enregistré avec success")
            return redirect('list_intervenant')
        else: return render(request,'add_intervenant.html',{'errors':form.errors,'form':form})
          
    else :
        form=IntervenantForm()
        context['form']=form
        return render(request,'add_intervenant.html',context)

def edit_intervenant(request,id):
    context={}
    instance=get_object_or_404(Intervenant,id=id)
    context['instance']=instance
    if request.method == "POST":
        form=IntervenantForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'edit successfuly !')
            return redirect('list_intervenant')
        else:
            return render(request,'edit_intervenant.html',context)
    else: 
        form=IntervenantForm(instance=instance)
        context['form']=form        
        return render(request,"edit_intervenant.html",context)

def delete_intervenant(request,id):
    if request.method =='POST':
        row=Intervenant.objects.get(id=id)
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_intervenant')
    else:
        context={}
        context['intervenant']=Intervenant.objects.get(id=id)
        context['transactions']=Transaction.objects.filter(customer=id)
        return render(request,'delete_intervenant.html',context)

def info_intervenant(request,id):
    context={}
    context['intervenant']=Intervenant.objects.get(id=id)
    context['transactions']=Transaction.objects.filter(intervenant=id)
    return render(request,'info_intervenant.html',context)

def list_transaction(request):
    context={}
    context['transactions']=Transaction.objects.all().order_by("date")
    if 'format' in request.GET :
       return get_data_table_file(request,Transaction)
    return render(request,'list_transaction.html',context)

def add_transaction(request):
    context={}
    context['categorys']=Category.objects.all().order_by('category')
    context['intervenants']=Intervenant.objects.all().order_by('intervenant')
    context['mouvements']=Mouvement.objects.all().order_by('mouvement')
    transactionForm=TransactionDataForm()
    if request.method=='POST':
        # On cree d'abord la facture
        intervenant=request.POST.get('intervenant')
        mouvement=request.POST.get('mouvement')
        full_quantity=request.POST.get('full_quantity')
        transaction_number=genererRef(Transaction,'TRA')
        instance=transactionForm.save(commit=False)
        intervenant=Intervenant.objects.get(id=intervenant)
        mouvement=Mouvement.objects.get(id=mouvement)
        instance.mouvement=mouvement
        instance.transaction_number=transaction_number
        instance.intervenant=intervenant
        instance.full_quantity=full_quantity
        instance.user=request.user
        instance.save()
        line_data = request.POST.getlist('lines[]')
        line_data=saveRow(line_data)
        for line in line_data:
            form = TransactionDataLineForm(line)
            if form.is_valid():
                line_instance = form.save(commit=False)
                line_instance.transaction = instance
                line_instance.save()  
        messages.success(request,"La Transaction a été enregistré avec success")
        return redirect("list_transaction")
        # On enregistre les differents lignes de facture
    elif  request.method=='GET':
        if 'fetchAll' in request.GET:
            data={}
            data['category']=list(Category.objects.all().values())
            data['article']=list(Article.objects.all().values())
            data['package']=list(Package.objects.all().values())
            return JsonResponse(data)
    context['transactionForm']=TransactionForm
    return render(request,'add_transaction.html',context)

def info_transaction(request,id):
    context={}
    context['transaction']=Transaction.objects.get(id=id)
    context['transactionLine']=TransactionLine.objects.filter(transaction=id)


    return render(request,'info_transaction.html',context)

def delete_transaction(request,id):
    context={}
    if request.method =='POST':
        row=Transaction.objects.get(id=id)
        detail=TransactionLine.objects.filter(transaction=id)
        detail.delete()
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_transaction')

    else:
        context['transaction']=Transaction.objects.get(id=id)
        context['transactionLine']=TransactionLine.objects.filter(transaction=id)
    return render(request,'delete_transaction.html',context)

def report_transaction(request):
    context={}
    if request.method == 'POST' :
        return calculate_stock_by_article('3')
        #return calculate_stock_article()
        if 'report_transaction' in request.POST: 
            pass
            
    else:
        context['transactions']=TransactionLine.objects.all().order_by('-id')
        context['articles']=Article.objects.all().order_by('-id')
        context['categorys']=Category.objects.all().order_by('-id')
        context['packages']=Package.objects.all().order_by('-id')
        context['intervenants']=Intervenant.objects.all().order_by('-id')
        
        reports=calculate_stock_article()
        print(reports)
        context['reports']=reports
        return render(request,"report_transaction.html",context)



