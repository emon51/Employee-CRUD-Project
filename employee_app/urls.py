
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),

    path('employee-list/', views.employees_list, name = 'employee-list'), 
    path('departments/', views.departments, name = 'departments'), 
    path('achievements/', views.achievements, name = 'achievements'), 

    path('add-department/', views.add_department, name = 'add-department'),
    path('add-achievement/', views.add_achievement, name = 'add-achievement'), 
    path('add-employee/', views.add_employee, name = 'add-employee'), 
]
