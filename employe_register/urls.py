from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employe_form,name="employe_insert"),
    path('<int:id>/',views.employe_form,name="employe_update"),
    path('delete/<int:id>/',views.employe_delete,name="employe_delete"),
    path('list/',views.employe_list,name="employe_list")
]