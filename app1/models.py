from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
 
class tab(models.Model):
    name = models.CharField(max_length=200)
    images=models.ImageField(upload_to='pro_img',default='')
    capacity=models.IntegerField(default='')
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class time(models.Model):
    date=models.DateTimeField()
    def __unicode__(self):
        return self.date
    
    
     
class Product(models.Model):
    category= models.ManyToManyField(category)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    des= models.TextField(default='')
    images=models.ImageField(upload_to='pro_img',default='')
    def __str__(self):
        return self.name

class Member(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=19)
    email = models.EmailField(default='')
    phone = models.IntegerField(default='max_length=10')
    
    def __str__(self):
        return self.username
        
        
class Order(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self):
        return self.name

        