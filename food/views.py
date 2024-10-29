from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import Userform
from .models import Dishlist


# Create your views here.
def welcome(request):
    list=Dishlist.objects.all()
    context={'names':list}
    return render(request,'food/main.html',context)

def create(request):
    form_instance=Userform()
    context = {'form':form_instance}
    return render(request,'food/form.html',context)

def accept(request):
    if request.method == "POST":
        filled_form = Userform(request.POST,request.FILES)
        if filled_form.is_valid():
            filled_form.save()
            return  redirect('welcome')
        
def edit(request,item_id):
    item=Dishlist.objects.get(id=item_id)
    edit_manual_form = Userform(instance=item)
    context= {'form':edit_manual_form,'item':item,}
    return render(request,'food/edit.html',context)


def update(request,item_id):
    if request.method == "POST":
        item = Dishlist.objects.get(id=item_id)
        form = Userform(request.POST,request.FILES,instance=item)
        context = {
            'form':form,
            'item':item,
        }
        if form.is_valid():
            form.save()
            return redirect('welcome')


def delete(request, item_id):
        item = Dishlist.objects.get(id=item_id)
        item.delete()
        return redirect('welcome')

