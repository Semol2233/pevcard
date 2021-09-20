# from django import forms
# from django.contrib.auth import authenticate


# class UserLoginForm(forms.Form):
#     username             = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password             = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


#     def clean(self , *args, **kwargs):
#         username         = self.cleaned_data.get('username')
#         password         = self.cleaned_data.get('password') 

#         if username and password:
#             user = authenticate(username=username,password=password)
#             if not user:
#                 raise forms.ValidationError('Wrong User!')
#             if not user.is_active:
#                 raise forms.ValidationError('Wrong User!')
#         return super(UserLoginForm,self).clean(*args, **kwargs)
       


from django import forms
from django.contrib.auth.models import User
from .models import *


class DateIssnput(forms.DateInput):
    input_type = 'date'

class card_pev_form(forms.ModelForm):
    class Meta:
        model = pevcard
        fields = ['user_name','user_id','User_Cardnumber','User_Card_status','User_Offerlist']
        widgets = {
            'user_name':forms.TextInput(attrs={'class':'form-control','placeholder':'User name'}),
            'user_id':forms.TextInput(attrs={'class':'form-control','placeholder':'User Id'}),
            'User_Cardnumber':forms.TextInput(attrs={'class':'form-control','placeholder':'User_Cardnumber'}),
            'User_Card_status': forms.CheckboxInput(attrs={'class': 'form-check-input','placeholder':'User name'}),  
       
    
          }


class DateIswwsnput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = "time"

class e_overtimeform(forms.ModelForm):
    class Meta:
        model = e_overtime
        fields = ['over_timehour','over_hour_in','over_hour_out','e_name','description']
        widgets = {
            'over_timehour':DateIswwsnput(attrs={'class':'form-control','placeholder':'User Id'}),
            'over_hour_in':TimeInput(attrs={'class':'form-control','placeholder':'User Id'}),
            'over_hour_out':TimeInput(attrs={'class':'form-control','placeholder':'User Id'}),
            'e_name':forms.Select(attrs={'class':'form-control','placeholder':'User Id'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Any Query'}),
         
          }



    def __init__(self,*args, **kwargs):
        super(e_overtimeform,self).__init__(*args, **kwargs)
        self.fields['e_name'].empty_label="Employ Name"
     
