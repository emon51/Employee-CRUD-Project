from django.shortcuts import render
from . models import Employee
from . forms import DepartmentForm, AchievementForm, EmployeeForm


# Create your views here.

#Home Page 
def home(request):
    return render(request, 'employee_app/home.html')


#Show All Employee
def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/employee_list.html', context = {'employees': employees})








