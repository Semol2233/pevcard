from django.shortcuts import render
#rest_framwork
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins,filters
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from django.http import HttpResponse
#end
from rest_framework.decorators import api_view
import random
import datetime
#user model
import jwt
from Data_app.models import *
#end
from datetime import datetime, timedelta
#serializer 
from Data_app.api.serializers import *
#end
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .pagination import PaginationHandlerMixin
#setting option
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#end
from django.contrib.auth.mixins import LoginRequiredMixin

# DJango built in login 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout
# end
from rest_framework.settings import api_settings
#social Auth 

#user filter
from django.contrib.auth import get_user_model
User = get_user_model()
#end
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView

from .date import datedata
from django import forms
#list view -> APi
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .forms import *















# def generate_jwt():
#     encoded_jwt = jwt.encode({'key': 'custom_value'}, 'secret', algorithm='HS256').decode('utf-8')
#     token = 'Bearer ' + encoded_jwt
#     return token

# jwt_token = generate_jwt()

    
# class Tag_ddviewr(pagination.PageNumberPagination):
#     page_size = 6
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# #mixpage_cahnnel player niche
# class mixchannel(generics.ListAPIView):
#     queryset               = post_models.objects.all().order_by('?')[:6]
#     serializer_class       = mixchannel
    


# #dtls page
# class ServiceDetailAPIView(generics.RetrieveAPIView):
#     queryset = post_models.objects.all()
#     serializer_class = ClassItemSerializer
#     lookup_field = ('channel_slug')



# #homepageapi
# class channelpost(APIView, PaginationHandlerMixin):
#     pagination_class = Tag_ddviewr

#     def get(self, request, category, *args, **kwargs):
#         authors = catgory_list.objects.filter(cat_slug=category).values('cat_name','cat_slug')
#         if authors:
#             posts = post_models.objects.filter(catgory__cat_slug=category).values('id','channel_name','channel_slug','straming_url','channel_logo','release_date').order_by('-id')

#             for author in list(authors):
#                 response = {
#                 'cat_name': author['cat_name']

#                 }
#             page = self.paginate_queryset(list(posts))
#             response['List'] = page
#             paginated_response = self.get_paginated_response(response)
#             return JsonResponse(paginated_response.data, safe=False)
#         return HttpResponse('No matching data found', status=404)



    
# class Tag_dsdviewr(pagination.PageNumberPagination):
#     page_size = 8
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# #payerpage
# class playerpagecatgory(APIView, PaginationHandlerMixin):
#     pagination_class = Tag_dsdviewr

#     def get(self, request, category, *args, **kwargs):
#         authors = catgory_list.objects.filter(cat_slug=category).values('cat_name','cat_slug')
#         if authors:
#             posts = post_models.objects.filter(catgory__cat_slug=category).values('id','channel_name','channel_slug','straming_url','channel_logo','release_date').order_by('-id')

#             for author in list(authors):
#                 response = {
#                 'cat_name': author['cat_name']

#                 }
#             page = self.paginate_queryset(list(posts))
#             response['List'] = page
#             paginated_response = self.get_paginated_response(response)
#             return JsonResponse(paginated_response.data, safe=False)
#         return HttpResponse('No matching data found', status=404)






# class postchannel(CreateView,LoginRequiredMixin):
#     form_class = daildddyscosst
#     model = post_models
#     template_name = 'uplode_us.html'




# class coverapi(generics.ListAPIView):
#     queryset               = coverimgapi.objects.all().order_by('-id')[:2]
#     serializer_class       = coverapiomg
    


# class nbox_adview(generics.ListAPIView):
#     queryset               = nbox_ad.objects.all()[:1]
#     serializer_class       = nbox_adapi
    





# class msgviewmodel(generics.ListAPIView):
#     queryset               = msgview.objects.all()[:1]
#     serializer_class       = msgseri
   


# class msgviewmodel(generics.ListAPIView):
#     queryset               = msgview.objects.all()[:1]
#     serializer_class       = msgseri
   



# class appsupdatmodel(generics.ListAPIView):
#     queryset               = appsupdate.objects.all()[:1]
#     serializer_class       = appsupdateseri
  
   


# class channel_Data(pagination.PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100





class Shadek(ListView):
    model = e_overtime
    template_name= 'query/query.html'
    
    def get_context_data(self, **kwargs):
         context = super(Shadek, self).get_context_data(**kwargs)
         context['fulllist'] = e_overtime.objects.filter(e_name__enamesd__contains='Shadek',over_timehour__range=datedata).order_by('over_timehour')
         context['count_working_days'] = e_overtime.objects.filter(e_name__enamesd__contains='Shadek',over_timehour__range=datedata).count()
         context['count_worksing_days'] = "Shadek"

         return context

class ridon(ListView):
    model = e_overtime
    template_name= 'query/query.html'
    
    def get_context_data(self, **kwargs):
         context = super(ridon, self).get_context_data(**kwargs)
         context['fulllist'] = e_overtime.objects.filter(e_name__enamesd__contains='ridon',over_timehour__range=datedata).order_by('over_timehour')
         context['count_working_days'] = e_overtime.objects.filter(e_name__enamesd__contains='ridon',over_timehour__range=datedata).count()
         context['count_worksing_days'] = "Ridon"


         return context



class Yeasin(ListView):
    model = e_overtime
    template_name= 'query/query.html'
    
    def get_context_data(self, **kwargs):
         context = super(Yeasin, self).get_context_data(**kwargs)
         context['fulllist'] = e_overtime.objects.filter(e_name__enamesd__contains='Yeasin',over_timehour__range=datedata).order_by('over_timehour')
         context['count_working_days'] = e_overtime.objects.filter(e_name__enamesd__contains='Yeasin',over_timehour__range=datedata).count()
         context['count_worksing_days'] = "Yeasin"

         return context

class Zia(ListView):
    model = e_overtime
    template_name= 'query/query.html'
    
    def get_context_data(self, **kwargs):
         context = super(Zia, self).get_context_data(**kwargs)
         context['fulllist'] = e_overtime.objects.filter(e_name__enamesd__contains='Zia',over_timehour__range=datedata).order_by('over_timehour')
         context['count_working_days'] = e_overtime.objects.filter(e_name__enamesd__contains='Zia',over_timehour__range=datedata).count()
         context['count_worksing_days'] = "Zia"


         return context



class Ridoy(ListView):
    model = e_overtime
    template_name= 'query/query.html'
    
    def get_context_data(self, **kwargs):
         context = super(Ridoy, self).get_context_data(**kwargs)
         context['fulllist'] = e_overtime.objects.filter(e_name__enamesd__contains='Ridoy',over_timehour__range=datedata).order_by('over_timehour')
         context['count_working_days'] = e_overtime.objects.filter(e_name__enamesd__contains='Ridoy',over_timehour__range=datedata).count()
         context['count_worksing_days'] = "Ridoy"
         return context

class Riyad_Driver(ListView):
    model = e_overtime
    template_name= 'query/query.html'
    
    def get_context_data(self, **kwargs):
         context = super(Riyad_Driver, self).get_context_data(**kwargs)
         context['fulllist'] = e_overtime.objects.filter(e_name__enamesd__contains='Riyad_Driver',over_timehour__range=datedata).order_by('over_timehour')
         context['count_working_days'] = e_overtime.objects.filter(e_name__enamesd__contains='Riyad_Driver',over_timehour__range=datedata).count()
         context['count_worksing_days'] = "Riyad_Driver"

         return context



class Riyad(ListView):
    model = e_overtime
    template_name= 'query/query.html'
    
    def get_context_data(self, **kwargs):
         context = super(Riyad, self).get_context_data(**kwargs)
         context['fulllist'] = e_overtime.objects.filter(e_name__enamesd__contains='Riyad',over_timehour__range=datedata).order_by('over_timehour')
         context['count_working_days'] = e_overtime.objects.filter(e_name__enamesd__contains='Riyad',over_timehour__range=datedata).count()
         context['count_worksing_days'] = "Riyad"

         return context





class Shakil(ListView):
    model = e_overtime
    template_name= 'query/query.html'
    
    def get_context_data(self, **kwargs):
         context = super(Shakil, self).get_context_data(**kwargs)
         context['fulllist'] = e_overtime.objects.filter(e_name__enamesd__contains='Shakil',over_timehour__range=datedata).order_by('over_timehour')
         context['count_working_days'] = e_overtime.objects.filter(e_name__enamesd__contains='Shakil',over_timehour__range=datedata).count()
         context['count_worksing_days'] = "Shakil"


         return context














# class playerpagedata(generics.ListAPIView):
#     queryset = post_models.objects.all().order_by('?')
#     serializer_class       = DRFPostSerializer
#     filter_backends        = [filters.SearchFilter]
#     search_fields          = ['catgory__cat_slug']
#     pagination_class       = channel_Data


# class channels_Data(pagination.PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# class homepagedata(generics.ListAPIView):
#     queryset = post_models.objects.all().order_by('?')
#     serializer_class       = DRFPostSerializer
#     filter_backends        = [filters.SearchFilter]
#     search_fields          = ['catgory__cat_slug']
#     pagination_class       = channels_Data










class pev_caduplodde(LoginRequiredMixin,CreateView):

    form_class = card_pev_form
    model = pevcard
    template_name = 'pevcad/pevcadup.html'





class router_lists(LoginRequiredMixin,ListView):
    model = pevcard
    template_name= 'pevcad/pevlist.html'
    
    def get_context_data(self, **kwargs):
         context = super(router_lists, self).get_context_data(**kwargs)
         context['router_list'] = pevcard.objects.all()
         context['totallist'] = pevcard.objects.all().count()
         return context






class over_timelistview(ListView):
    model = e_overtime
    template_name= 'pevcad/overtime.html'
    
    def get_context_data(self, **kwargs):
         context = super(over_timelistview, self).get_context_data(**kwargs)
         context['overtime'] = e_overtime.objects.all().order_by('-over_timehour')
         return context



class e_post_overtime(LoginRequiredMixin,CreateView):
    form_class = e_overtimeform
    model = e_overtime
    template_name = 'pevcad/overtimeup.html'




class postupdate(LoginRequiredMixin,UpdateView):
    form_class = e_overtimeform
    model = e_overtime
    template_name = 'pevcad/overtimeup.html'


