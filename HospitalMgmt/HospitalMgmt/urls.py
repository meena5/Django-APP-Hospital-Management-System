"""HospitalMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from hospital.views import *


urlpatterns = [
    path('',include('hospital.urls')),
    path('admin/', admin.site.urls),
    
    path('about/', About,name='about'),
    path('contact/', Contact,name='contact'),
    path('admin_login/', Login,name='login'),
    path('logout/', Logout_admin,name='logout'),
    path('view_doctor/',View_Doctor,name='view_doctor'),

    path('view_patient/',View_Patient,name='view_patient'),

    path('view_appointment/',View_Appointment,name='view_appointment'),

    path('add_appointment/',Add_Appointment,name='add_appointment'),
    path('add_doctor/',Add_Doctor,name='add_doctor'),

    path('add_patient/',Add_Patient,name='add_patient'),
    path('delete_doctor(?p<int:pid>)',Delete_Doctor,name='delete_doctor'),
    path('edit_doctor(?p<int:pid>)',Edit_Doctor,name='edit_doctor'),
    path('delete_patient(?p<int:pid>)',Delete_Patient,name='delete_patient'),

     path('delete_appointment(?p<int:pid>)',Delete_Appointment,name='delete_appointment'),




]
