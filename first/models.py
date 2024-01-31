
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Variant(models.Model):
    variant=models.CharField(max_length=100,primary_key=True)
    
    
    def __str__(self):
      return self.variant

class Brand(models.Model):
    brand=models.CharField(max_length=100,primary_key=True)

    
    def __str__(self):
      return self.brand

class Cars(models.Model):
    name=models.CharField(max_length=100)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    variant=models.ForeignKey(Variant,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='carimg',null=True)
    price=models.CharField(max_length=400)
    feature1=models.CharField(max_length=400,blank=True)
    feature2=models.CharField(max_length=400,null=True,blank=True)
    feature3=models.CharField(max_length=400,null=True,blank=True)
    feature4=models.CharField(max_length=400,null=True,blank=True)
    feature5=models.CharField(max_length=400,null=True,blank=True)
    feature6=models.CharField(max_length=400,null=True,blank=True)
    feature7=models.CharField(max_length=400,null=True,blank=True)
    feature8=models.CharField(max_length=400,null=True,blank=True)
    feature9=models.CharField(max_length=400,null=True,blank=True)

    

    
    def __str__(self):
      return self.name
