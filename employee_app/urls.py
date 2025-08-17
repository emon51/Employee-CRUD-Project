
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('employee_list/', views.employees_list, name = 'employee_list'), 
    path('departments/', views.departments, name = 'departments'), 
    path('achievements/', views.achievements, name = 'achievements'), 
]
