from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User



class DevName(models.Model):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
        


class Video(models.Model):
    devname =models.ForeignKey(DevName, on_delete=CASCADE)    
    video= models.FileField(upload_to='videos/')   
    

""" class review(models.Model):
    links =models.ForeignKey(links, on_delete=CASCADE)    
    review= models.CharField(max_length=200)   

    def __str__(self):
        return self.review """