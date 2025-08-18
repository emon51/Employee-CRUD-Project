
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),

    path('employee-list/', views.employees_list, name = 'employee-list'), 
    path('departments/', views.departments, name = 'departments'), 
    path('achievements/', views.achievements, name = 'achievements'), 

    path('add-department/', views.add_department, name = 'add-department'),
    path('add-achievement/', views.add_achievement, name = 'add-achievement'), 
    path('add-employee/', views.add_employee, name = 'add-employee'), 

    path('update-employee/<int:id>', views.update_employee, name = 'update-employee'), 
    path('delete-employee/<int:id>', views.delete_employee, name = 'delete-employee'), 

    path('update-department/<int:id>', views.update_department, name = 'update-department'), 
    path('update-achievement/<int:id>', views.update_achievement, name = 'update-achievement'), 

    path('delete-department/<int:id>', views.delete_department, name = 'delete-department'), 
    path('delete-achievement/<int:id>', views.delete_achievement, name = 'delete-achievement'), 
]
