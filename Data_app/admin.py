from django.contrib import admin
admin.site.site_header = "NVS-PEV-CARD"

from .models import pevcard,Userofferlist
admin.site.register(pevcard)
admin.site.register(Userofferlist)












