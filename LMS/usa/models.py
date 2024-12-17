from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y')
    
    def __str__(self):
        return self.title

class fullsail(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y')
    
    def __str__(self):
        return self.title
class coloradostate(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y')
    
    def __str__(self):
        return self.title
class oregonstate(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y')
    
    def __str__(self):
        return self.title
class saintlouis(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y')
    
    def __str__(self):
        return self.title