from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Data_app import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('homepage/<category>', channelpost.as_view()),
    # path('plyerpage/<category>', playerpagecatgory.as_view()),
    # path('d/<channel_slug>', ServiceDetailAPIView.as_view()),
     path('', router_lists.as_view(),name='homes'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('login/',LoginView.as_view(),name='login'),
     path('up/',pev_caduplodde.as_view(),name='up'),
     path('postovertime/',e_post_overtime.as_view(),name='up'),
     path('list/',over_timelistview.as_view(),name='listover'),
     path('upover/<int:pk>/',postupdate.as_view(),name='upovser'),




     

    # path('add', postchannel.as_view(),name='fhdf'), 
    # path('cover', coverapi.as_view(),name='ee'),
    # path('ad', nbox_adview.as_view(),name='ad'),
    # path('msg', msgviewmodel.as_view(),name='awd'),
    # path('up', appsupdatmodel.as_view(),name='update'),

    # path('home', playerpagedata.as_view(),name='ch'),
    # path('dtls', homepagedata.as_view(),name='ch')




    

]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#mix url - its player niche prthom akta mix channel hbe 
#d/ player page dtls pagfe
#cat catagory ghulo get kora

