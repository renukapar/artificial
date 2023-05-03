from django.shortcuts import render,HttpResponseRedirect
from .models import ImageModel,UploadVideo
from .forms import ImageForm,UploadForm
# Create your views here.
def pimgshow(r):
    pimg=ImageModel.objects.all()
    return render(r,'prod/pimgshow.html',{'pimg':pimg})
def pimgform(r):
    form=ImageForm()
    if r.method=='POST':
        form=ImageForm(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    return render(r,'prod/vimgform.html',{'form':form})
def videoshow(r):
    vimg=UploadVideo.objects.all()
    return render(r,'prod/videoshow.html',{'vimg':vimg})
def videoupload(r):
    if r.method == 'POST':
        form =UploadForm(r.POST, r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jp')
    return render(r, 'prod/vupload.html', {"form": form})