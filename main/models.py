from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class DevName(models.Model):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class External(models.Model):
    devname=models.ForeignKey(DevName, on_delete=CASCADE) 
    book= models.URLField(blank=True) 
    yt= models.URLField(blank=True) 
    doc= models.URLField(blank=True) 

class Review(models.Model):
    devname=models.ForeignKey(DevName, on_delete=CASCADE, default='1')
    user=models.ForeignKey(User, on_delete=PROTECT)
    review= models.TextField(max_length=500)

    def __str__(self):
        return self.review
    
class Question(models.Model):
    question = models.CharField(max_length=300)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correct_option = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])

    def __str__(self):
        return self.question

class Video(models.Model):
    questions = models.ManyToManyField(Question)
    devname =models.ForeignKey(DevName, on_delete=CASCADE)    
    video= models.FileField(upload_to='videos/')

