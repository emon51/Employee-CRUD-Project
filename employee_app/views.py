from django.shortcuts import render, redirect
from . models import Employee, Department, Achievement, AchievementEmployee
from . forms import DepartmentForm, AchievementForm, EmployeeForm

# Create your views here.

# Home Page 
def home(request):
    return render(request, 'employee_app/home.html')


# Show employee list 
def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/employee_list.html', context = {'employees': employees})



# Show department list 
def departments(request):
    depts = Department.objects.all()
    return render(request, 'employee_app/departments.html', context = {'departments': depts})



# Show achievement list
def achievements(request):
    all_achivement = Achievement.objects.all()
    return render(request, 'employee_app/achievements.html', context = {'achievements': all_achivement})



# Adding new department
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')
    else:
        form = DepartmentForm()
    return render(request, "employee_app/add.html", {"form": form})


    



# Adding new achievement
def add_achievement(request):
    if request.method == "POST":
        form = AchievementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('achievements')
    else:
        form = AchievementForm()
    return render(request, "employee_app/add.html", {"form": form})


    



# Adding new employee
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
    else:
        form = EmployeeForm()
    return render(request, "employee_app/add.html", {"form": form})

    













