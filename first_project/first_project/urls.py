"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import home,addition_opt,subtraction_opt, multiplication_opt, division_opt,modulus_opt, exponentation_opt, floor_division
from first_app.views import emp_details,create_emp_details,emp_details_form_home,delete_emp_details,update_emp_details
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('addition/', addition_opt),
    path('subtraction/', subtraction_opt),
    path('multiplication/', multiplication_opt),
    path('division/', division_opt),
    path('modulus/', modulus_opt),
    path('exponentation/', exponentation_opt),
    path('floor division/', floor_division),
    path('emp_details/', emp_details,name="emp_details_url"),
    path('emp_details_form_home/', emp_details_form_home,name="emp_details_form_home"),
    path('emp_details_form/', create_emp_details,name="emp_details_form"),
    path('delete_emp_details/<pk>', delete_emp_details,name="delete_empdetail_url"),
    path('update_emp_details/<pk>', update_emp_details,name="update_emp_details_url"),
    path('update_emp_details_data/', update_emp_details, name="update_emp_details_data_url"),



]
