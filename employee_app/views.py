from django.shortcuts import render, redirect, get_object_or_404
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



# Update employee
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
def delete_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('employee-list')


# Delete department 
def delete_department(request, id):
    dept = get_object_or_404(Department, pk=id)
    dept.delete()
    return redirect('departments')

# Delete achivement 
def delete_achievement(request, id):
    ach = get_object_or_404(Achievement, pk=id)
    ach.delete()
    return redirect('achievements')


    













