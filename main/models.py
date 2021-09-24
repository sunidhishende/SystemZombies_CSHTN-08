from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth.models import User



class DevName(models.Model):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
        


class Video(models.Model):
    devname =models.ForeignKey(DevName, on_delete=CASCADE)    
    video= models.FileField(upload_to='videos/') 

class External(models.Model):
    devname=models.ForeignKey(DevName, on_delete=CASCADE) 
    book= models.URLField(blank=True) 
    yt= models.URLField(blank=True) 
    doc= models.URLField(blank=True) 

class Review(models.Model):
    user=models.OneToOneField(User, on_delete=PROTECT)
    review= models.CharField(max_length=500)
    
    

