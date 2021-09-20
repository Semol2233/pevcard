from django.contrib import admin
admin.site.site_header = "NVS-PEV-CARD"

from .models import pevcard,Userofferlist,ename,e_overtime
admin.site.register(pevcard)
admin.site.register(Userofferlist)

admin.site.register(ename)
admin.site.register(e_overtime)













