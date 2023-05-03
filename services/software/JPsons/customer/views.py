from django.shortcuts import render,HttpResponseRedirect
from.models import CustomerModel
from .forms import CustomerForm,SignForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(r):
    return render(r,'cust/home.html')
def cshow(r):
    cust=CustomerModel.objects.all()
    return render(r,'cust/cshow.html',{'cust':cust})
def cform(r):
    form=CustomerForm
    if r.method=='POST':
        form=CustomerForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jp')
    return render(r,'cust/cform.html',{'form':form})
@login_required()
def signup(r):
    form = SignForm
    if r.method == 'POST':
        form =SignForm(r.POST)
        abc=form.save()
        abc.set_password(abc.password)
        abc.save()
        return HttpResponseRedirect('/jp')
    return render(r,'cust/sign.html', {'form': form})
def logout(r):
    return render(r, 'cust/logout.html')
def insert(r):
    form=CustomerForm()
    if r.method=='POST':
        form=CustomerForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jp')
    return render(r,'cust/cinsert.html',{'form':form})
def update(r,id):
    obj=CustomerModel.objects.get(id=id)
    form = CustomerForm()
    if r.method == 'POST':
        form = CustomerForm(r.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jp')
    return render(r, 'cust/cupdate.html', {'obj': obj})
def delete(r,id):
    obj=CustomerModel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(r,'/jp')


