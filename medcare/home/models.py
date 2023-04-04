from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    user=models.ForeignKey(User, on_delete= models.CASCADE ,null=True, blank=True)
    otp_code=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.user.username