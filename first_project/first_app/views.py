from contextlib import contextmanager

from django.shortcuts import render, HttpResponse, redirect
from .models import EmpDetails

# Create your views here.
def emp_details(request):
    # database operation to read the data from table
    # Select * from EmpDetails
    details=EmpDetails.objects.all()


    # Select * from EmpDetails where emp_name="sonu"
    # single_data = EmpDetails.objects.get(emp_name="sonu")
    # print(single_data)


    context ={'details':details}

    # context ={'single_data': single_data}


    # return HttpResponse("emp_details")
    return render(request,"EmpDetails.html",context)
def emp_details_form_home(request):
    return render(request, "EmpDetails_form.html")

def create_emp_details(request):
    msg = "not saved"
    if request.method=="POST":
        # get the form data
        emp_name_form= request.POST['EmpName']
        emp_city_form=request.POST['EmpCity']
        emp_company_form=request.POST['EmpCompany']
        # print('emp_name')

        # save the form data into db
        EmpDetails(emp_name=emp_name_form,
                   emp_city=emp_city_form,
                   emp_company=emp_company_form).save()
        msg="data saved"

    context={'msg':msg}
    return render(request,"EmpDetails_form.html",context)

def delete_emp_details(request,pk):
    data=EmpDetails.objects.get(id=pk)
    data.delete()
    details = EmpDetails.objects.all()
    context = {'details': details}

    return render(request,"EmpDetails.html",context)



def update_emp_details(request,pk=None):
    if request.method == "POST":
        # get the form data
        emp_id_form = request.POST['EmpID']

        # Data from Database
        single_data = EmpDetails.objects.get(id=emp_id_form)

        # Updated Form Data
        emp_name_form = request.POST['EmpName']
        emp_city_form = request.POST['EmpCity']
        emp_company_form = request.POST['EmpCompany']

        single_data.emp_name=emp_name_form
        single_data.emp_city=emp_city_form
        single_data.emp_company=emp_company_form

        single_data.save()


        # print(emp_name_form)
        return redirect("emp_details_url")

        # Fetch the data
        # Select * from EmpDetails where id=pk;
    if pk:
            single_data = EmpDetails.objects.get(id=pk)
        # print(data)
            context = {'single_data': single_data}
            return render(request, "EmpDetails_update.html", context)



