from django.shortcuts import render
from django.http import HttpResponse
from.models import DevName, Video
from .forms import AddNewResources
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html',{})


@login_required(login_url='/login')
def video(request, id):
    devname= DevName.objects.get(id= id)
    return render(request,'videos.html',{"devname":devname})



""" def video(request):
    video= Video.objects.all()
    print(video)
    return render(request,"main/videos.html",{"video":video}) """





""" def sendresources(response):
      if response.method=="POST":
         form=AddNewResources(response.POST)
         if form.is_valid():
                n=form.cleaned_data["name"]
                


      else :
         form= AddNewResources()

      return render(response,"main/sendresources.html",{"form": form })
 """