from django.shortcuts import render
from . models import Employee, Department, Achievement, AchievementEmployee


# Create your views here.

#Home Page 
def home(request):
    return render(request, 'employee_app/home.html')


#Show All Employee
def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/employee_list.html', context = {'employees': employees})


def departments(request):
    depts = Department.objects.all()
    return render(request, 'employee_app/departments.html', context = {'departments': depts})


def achievements(request):
    all_achivement = Department.objects.all()
    return render(request, 'employee_app/achievements.html', context = {'achievements': all_achivement})











