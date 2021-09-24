from django.shortcuts import render
from django.http import HttpResponse
from.models import DevName, User, Review
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

@login_required(login_url='/login')
def review(request):
    devname= DevName.objects
    if request.method=="POST":
       r=request.POST.get('text')
       a=request.POST.get('devnames')
       current_user= request.user
       b=devname.get(id=a)
       t= User.objects.get(id= current_user.id)
       review = Review.objects.create(user=t,devname=b,review=r)
       review.save()
    return render(request,'feedback.html', {"devname":devname})

