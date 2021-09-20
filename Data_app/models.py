from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
# from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.urls import reverse



# class catgory_list(models.Model):
#     cat_name           = models.CharField(max_length=255)
#     release_date       = models.DateField(auto_now_add = True)
#     cat_slug           =   models.SlugField(max_length=200)

#     def __str__(self):
#         return self.cat_name   


# class post_models(models.Model):
#     channel_name   = models.CharField(max_length=255)
#     channel_slug =   models.SlugField(max_length=200)
#     catgory        = models.ForeignKey(catgory_list,blank=True,on_delete=CASCADE)
#     release_date   = models.DateField(auto_now_add = True)
#     straming_url =  models.URLField(default='www.test.com')
#     channel_logo   = models.FileField(upload_to="channel_logo" ,blank=True)

#     def __str__(self):
#         return self.channel_name    


#     def get_absolute_url(self):
#         return reverse('fhdf')




# class coverimgapi(models.Model):
#     release_date   = models.DateField(auto_now_add = True)
#     channel_logo   = models.FileField(upload_to="coverimg" ,blank=True)




# class nbox_ad(models.Model):
#     release_date   = models.DateField(auto_now_add = True)
#     status = models.BooleanField(default=False)
#     ad_img   = models.FileField(upload_to="coverimg" ,blank=True)


# class msgview(models.Model):
#     release_date   = models.DateField(auto_now_add = True)
#     status = models.BooleanField(default=False)
#     msg = models.TextField(blank=True)
   

#     def __str__(self):
#         return self.msg    


# class appsupdate(models.Model):
#   videourl =   models.URLField(max_length=300)
#   msg = models.TextField(blank=True)
#   updatelinkbutton = models.URLField(max_length=300)

class Userofferlist(models.Model):
    offer          = models.CharField(max_length=100)
    offer_parcent = models.CharField(max_length=255,default="10%")
    created_date   = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.offer 

class pevcard(models.Model):
    created_date   = models.DateTimeField(default=timezone.now)
    Date =  models.DateField(auto_now_add = True)
    user_name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    User_Cardnumber = models.CharField(max_length=255)
    User_Card_status = models.BooleanField(default=False)
    User_Offerlist = models.ManyToManyField('Userofferlist')

    def __str__(self):
        return self.user_name 

    def get_absolute_url(self):
        return reverse('homes')

class ename(models.Model):
    enamesd = models.CharField(max_length=255)

    def __str__(self):
        return self.enamesd 

class e_overtime(models.Model):
    over_timehour   = models.DateField()
    over_hour_in    = models.TimeField()
    over_hour_out   = models.TimeField(blank=True,null=True)
    Date =  models.DateField(auto_now_add = True)
    e_name = models.ForeignKey(ename,blank=True,on_delete=CASCADE)
    description = models.TextField(blank=True)
   

    def __str__(self):
        return self.e_name.enamesd

    def get_absolute_url(self):
        return reverse('listover')



