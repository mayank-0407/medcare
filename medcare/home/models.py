from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    user=models.ForeignKey(User, on_delete= models.CASCADE ,null=True, blank=True)
    otp_code=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
class MedType(models.Model):
    name=models.CharField(max_length=100,null=True)
    code=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name
    
class Medicine(models.Model):

    mycustomer=models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=100,null=True)
    price=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)
    description=models.TextField(null=True)
    expire_date=models.DateField(null=True)
    type=models.ForeignKey(MedType,on_delete=models.SET_NULL,max_length=20,null=True)

    def __str__(self):
        return self.name