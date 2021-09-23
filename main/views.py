from django.shortcuts import render
from django.http import HttpResponse
from.models import DevName
from .forms import AddNewResources
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html',{})


@login_required(login_url='/login')
def video(request, id):
    devname= DevName.objects.get(id= id)
    return render(request,'videos.html',{"devname":devname})

@login_required(login_url='/login')
def external(request, id):
    devname= DevName.objects.get(id= id)
    return render(request,'external.html',{"devname":devname})






""" def sendresources(response):
      if response.method=="POST":
         form=AddNewResources(response.POST)
         if form.is_valid():
                n=form.cleaned_data["name"]
                


      else :
         form= AddNewResources()

      return render(response,"main/sendresources.html",{"form": form })
 """