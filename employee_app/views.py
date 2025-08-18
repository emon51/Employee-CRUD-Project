from django.shortcuts import render, redirect, get_object_or_404
from . models import Employee, Department, Achievement, AchievementEmployee
from . forms import DepartmentForm, AchievementForm, EmployeeForm

from django.contrib.auth.decorators import login_required

# Create your views here.

# Home Page 

@login_required
def home(request):
    return render(request, 'employee_app/home.html')


# Show employee list 

@login_required
def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/employee_list.html', context = {'employees': employees})



# Show department list 

@login_required
def departments(request):
    depts = Department.objects.all()
    return render(request, 'employee_app/departments.html', context = {'departments': depts})



# Show achievement list

@login_required
def achievements(request):
    all_achivement = Achievement.objects.all()
    return render(request, 'employee_app/achievements.html', context = {'achievements': all_achivement})



# Adding new department

@login_required
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

@login_required
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

@login_required
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
    else:
        form = EmployeeForm()
    return render(request, "employee_app/add.html", {"form": form})



# Update employee

@login_required
def update_employee(request, id):
    employee = get_object_or_404(Employee, pk=id) 
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee-list") 
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employee_app/update.html", {"form": form})





# Delete employee

@login_required 
def delete_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('employee-list')



# Update department 

@login_required
def update_department(request, id):
    dept = get_object_or_404(Department, pk=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('departments')
    else:
        form = DepartmentForm(instance=dept)
    return render(request, 'employee_app/update.html', context = {'form': form})



# Update achievement

@login_required
def update_achievement(request, id):
    achievement = get_object_or_404(Achievement, pk=id)
    if request.method == 'POST':
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            form.save()
            return redirect('achievements')
    else:
        form = AchievementForm(instance=achievement)
    return render(request, 'employee_app/update.html', context = {'form': form})





# Delete department

@login_required
def delete_department(request, id):
    dept = get_object_or_404(Department, pk=id)
    dept.delete()
    return redirect('departments')




# Delete achivement 

@login_required
def delete_achievement(request, id):
    ach = get_object_or_404(Achievement, pk=id)
    ach.delete()
    return redirect('achievements')


    













