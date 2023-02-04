from django.db import models

# Create your models here.
class registerdb(models.Model):
    full_name = models.CharField(max_length=40, null=True, blank=True)
    username = models.CharField(max_length=40, null=True, blank=True)
    mobile_number= models.IntegerField( null=True, blank=True)
    Email = models.EmailField(max_length=40, null=True, blank=True)
    password = models.CharField(max_length=40, null=True, blank=True)
    repassword = models.CharField(max_length=100, null=True, blank=True)


