from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .functions import *
from .forms import *
# Create your views here.



def welcome(request):
    context={}
    return render(request,'welcome.html',context)

def list_category(request):
    context={}
    form=CategoryForm()    

    context['form']=form
    context['categorys']=Category.objects.all().order_by('-id')

    if 'format' in request.GET:
        return get_data_table_file(request,Category)
    return render(request,'list_category.html',context)
    
# Donwload table html 
def download_file_type(request):
    
    if 'format' in request.GET :
       print('Okay')
       return export_data(request,Article)

# procedure pour creer une category
def add_category(request):
    context={}
    if request.method =="POST":
        
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            messages.success(request,"la categorie a été enregistré avec success")
            return redirect('list_category')
        else: return render(request,'add_category.html',{'errors':form.errors,'form':form})
          
    else :
        form=CategoryForm()
        context['form']=form
        return render(request,'add_category.html',context)

# procedure pour Modifier une category
def edit_category(request,id):
    context={}
    instance=get_object_or_404(Category,id=id)
    context['instance']=instance
    if request.method == "POST":
        form=CategoryForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request,'edit successfuly !')
            return redirect('list_category')
        else:
            return render(request,'edit_category.html',context)
    else: 
        form=CategoryForm(instance=instance)
        context['form']=form        
        return render(request,"edit_category.html",context)

# procedure pour Supprimer une category
def delete_category(request,id):
    if request.method =='POST':
        row=Category.objects.get(id=id)
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_category')
    else:
        context={}
        context['category']=Category.objects.get(id=id)
        context['articles']=Article.objects.filter(category=id)
        return render(request,'delete_category.html',context)

def info_category(request,id):
    context={}
    context['category']=Category.objects.get(id=id)
    context['articles']=Article.objects.filter(category=id)
    return render(request,'info_category.html',context)


def list_package(request):
    context={}
    form=PackageForm()
    if request.method=="POST":
        pass
    else:
        if 'format' in request.GET :
            return get_data_table_file(request,Package)
        context['form']=form
        context['packages']=Package.objects.all().order_by('-id')
    
        return render(request,'list_package.html',context)


# procedure pour creer un Emballage
def add_package(request):
    context={}
    if request.method =="POST":
        
        form=PackageForm(request.POST)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            messages.success(request,"la categorie a été enregistré avec success")
            return redirect('list_package')
        else: return render(request,'add_package.html',{'errors':form.errors,'form':PackageForm()})
          
    else :
        form=PackageForm()
        context['form']=form
        return render(request,'add_package.html',context)

# procedure pour Modifier un Emballage
def edit_package(request,id):
    context={}
    instance=get_object_or_404(Package,id=id)
    context['instance']=instance
    if request.method == "POST":
        form=PackageForm(request.POST,instance=instance)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.save()
            messages.success(request,'edit successfuly !')
            return redirect('list_package')
        else:
            return render(request,'edit_package.html',context)
    else: 
        form=PackageForm(instance=instance)
        context['form']=form        
        return render(request,"edit_package.html",context)

# procedure pour Supprimer un Emballage
def delete_package(request,id):
    if request.method =='POST':
        row=Package.objects.get(id=id)
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_package')
    else:
        context={}
        context['package']=Package.objects.get(id=id)
        context['articles']=Article.objects.filter(package=id)
        return render(request,'delete_package.html',context)

def info_package(request,id):
    context={}
    context['package']=Package.objects.get(id=id)
    context['articles']=Article.objects.filter(package=id)
    return render(request,'info_package.html',context)

# procedure pour creer une category
def add_article(request):
    context={}
    if request.method =="POST":
        
        form=ArticleForm(request.POST,request.FILES)
        ref=genererRef(Article,"ART")
        if form.is_valid:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.article_number=ref
            instance.save()
            messages.success(request,"la categorie a été enregistré avec success")
            return redirect('list_article')
        else: return render(request,'add_article.html',{'errors':form.errors,'form':ArticleForm()})
          
    else :
        form=ArticleForm()
        context['form']=form
        return render(request,'add_article.html',context)

# procedure pour Modifier une category
def edit_article(request,id):
    context={}
    instance=get_object_or_404(Article,id=id)
    context['instance']=instance
    if request.method == "POST":
        form=ArticleForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            f.save()
            messages.success(request,'edit successfuly !')
            return redirect('list_article')
        else:
            return render(request,'edit_article.html',context)
    else: 
        form=ArticleForm(instance=instance)
        context['form']=form        
        return render(request,"edit_article.html",context)

# procedure pour Supprimer une category
def delete_article(request,id):
    if request.method =='POST':
        row=Article.objects.get(id=id)
        row.delete()
        messages.success(request,"Delete Successfully !!!")
        return redirect('list_article')
    else:
        context={}
        context['article']=Article.objects.get(id=id)
        return render(request,'delete_article.html',context)

def info_article(request,id):
    context={}
    context['article']=Article.objects.get(id=id)
    context['articles']=Article.objects.filter(category=id)
    return render(request,'info_article.html',context)


def list_article(request):
    context={}
    form=ArticleForm()

    if request.method=='POST':
        pass  
    else:
        if 'format' in request.GET :
            #return get_data_table_file(request,Article)
            return export_data(request,Article)
        
        context['form']=form
        context['articles']=Article.objects.all().order_by('-id')
        return render(request,'list_article.html',context)