from django.db import models

# Create your models here.

class categorydb(models.Model):
    add_ct_name = models.CharField(max_length=40, null=True, blank=True)
    add_ct_dsc = models.CharField(max_length=100, null=True, blank=True)
    add_ct_profile = models.ImageField(upload_to="profile",null=True,blank=True)


class productdb(models.Model):
    add_pdt_category = models.CharField(max_length=40, null=True, blank=True)
    add_pdt_brand = models.CharField(max_length=40, null=True, blank=True)
    add_pdt_name = models.CharField(max_length=40, null=True, blank=True)
    add_pdt_dsc = models.CharField(max_length=100, null=True, blank=True)
    add_pdt_size = models.CharField(max_length=40, null=True, blank=True)
    add_pdt_price = models.CharField(max_length=40, null=True, blank=True)
    add_pdt_profile_1 = models.ImageField(upload_to="profile",null=True,blank=True)
    add_pdt_profile_2 = models.ImageField(upload_to="profile",null=True,blank=True)
    add_pdt_profile_3 = models.ImageField(upload_to="profile",null=True,blank=True)

class branddb(models.Model):
    add_bd_name = models.CharField(max_length=40, null=True, blank=True)
    add_bd_dsc = models.CharField(max_length=100, null=True, blank=True)
    add_bd_profile = models.ImageField(upload_to="profile",null=True,blank=True)



class sizedb(models.Model):
    size_ltr = models.CharField(max_length=40, null=True, blank=True)
    size_num = models.IntegerField(null=True, blank=True)


class contact_us_db(models.Model):
    contact_name=models.CharField(max_length=100,null=True,blank=True)
    contact_email=models.EmailField(max_length=100,null=True,blank=True)
    contact_message=models.CharField(max_length=1000,null=True,blank=True)








