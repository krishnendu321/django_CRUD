from django.shortcuts import render,redirect
from .forms import EmployeForm
from .models import Employe

# Create your views here.
def employe_list(request):
    context={'employe_list': Employe.objects.all()}
    return render(request,"employe_register/employe_list.html",context)

def employe_form(request,id=0):

    if request.method == "GET":
        if id==0:
            form =EmployeForm()
        else:
            employe=Employe.objects.get(pk=id)
            form=EmployeForm(instance=employe)
            
        return render(request,"employe_register/employe_form.html",{'form': form})
        
    else:
        if id==0:
            form= EmployeForm(request.POST)
        else:
            employe1=Employe.objects.get(pk=id)
            form= EmployeForm(request.POST,instance=employe1)
        if form.is_valid():
            form.save()
        return redirect('/employe/list')

def employe_delete(request,id):
    employe=Employe.objects.get(pk=id)
    employe.delete()

    return redirect('/employe/list')
