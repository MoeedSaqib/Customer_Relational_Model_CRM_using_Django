from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    user=models.OneToOneField(User , null=True ,blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True) 
    phone=models.CharField(max_length=200, null=True) 
    email=models.CharField(max_length=200, null=True) 
    profilepic=models.ImageField ( default="www.png" ,null=True , blank=True)
    date=models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):
     return self.name
        

 

class Tag(models.Model):
    name=models.CharField(max_length=200, null=True) 
    
    def __str__(self):
     return self.name
        


class Product(models.Model):
         CATEGORY=(
           ('Indoor','Indoor'),
           ('Outdoor','Outdoor'),
           )
      
         name = models.CharField(max_length=200, null=True)
         price = models.FloatField( null=True)
         category = models.CharField(max_length=200, null=True, choices=CATEGORY) 
         description = models.CharField(max_length=200, null=True , blank=True) 
         date = models.DateTimeField(auto_now_add=True, null=True) 
         tags = models.ManyToManyField(Tag)
         def __str__(self):
          return self.name
 
        


class Orders(models.Model):
       STATUS=(
           ('Pending','Pending'),
           ('Out for Delivery','Out for Delivery'),
           ('Delivered','Delivered'),
       )
       customer= models.ForeignKey(customer , null=True , on_delete=models.SET_NULL)
       product=  models.ForeignKey(Product , null=True , on_delete=models.SET_NULL)
       status=models.CharField(max_length=200, null=True, choices=STATUS) 
       date=models.DateTimeField(auto_now_add=True, null=True) 
       note=models.CharField(max_length=800, null=True) 
       def __str__(self):
         return self.product
        
