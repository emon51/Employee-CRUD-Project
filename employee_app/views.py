from django.shortcuts import render
from . models import Employee


# Create your views here.

def home(request):
    return render(request, 'employee_app/home.html')

def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/employee_list.html', context = {'employees': employees})





