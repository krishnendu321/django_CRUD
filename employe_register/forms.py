from django import forms
from .models import Employe
class EmployeForm(forms.ModelForm):

    class Meta:
        model= Employe
        fields={'fullname','mobile','empcode','position'}
        labels={
            "fullname" : "Full Name",
            
            "empcode" : "Emp Code"
            


        }
    def __init__(self,*args,**kwargs):
        super(EmployeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="Select "
        self.fields['empcode'].required= False

