from django.shortcuts import render,HttpResponseRedirect
from .models import ProductModel
from .forms import ProductForm
from .serialization import Productser
from rest_framework import request,response,status
from rest_framework.views import Response,APIView

# Create your views here.
def pshow(r):
    prod=ProductModel.objects.all()
    return render(r,'prod/pshow.html',{'prod':prod})
def pform(r):
    form=ProductForm
    if r.method=='POST':
        form=ProductForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    return render(r,'prod/pform.html',{'form':form})
class papiview(APIView):
    def get(self,r):
        pobj=ProductModel.objects.all()
        pser=Productser(pobj,many=True)
        return Response(pser.data)
    def post(self,r):
        serobj=Productser(data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)
class papidel(APIView):
    def put(self,r,pk):
        obj=ProductModel.objects.get(pk=pk)
        seobj=ProductForm(obj,data=r.data)
        if seobj.is_valid():
            seobj.save()
            return Response(seobj.data, status=status.HTTP_201_CREATED)
        return Response(seobj.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,r,pk):
        obj=ProductModel.objects.get(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)







