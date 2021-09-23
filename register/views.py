from django.shortcuts import render 
from .forms import RegistrationForm


def register(request):
    if request.method=="POST": 
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
         
    else:
      form=RegistrationForm()
    return render(request, "register.html", {"form": form})
