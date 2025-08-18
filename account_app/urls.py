
from django.urls import path 
from . import views 

urlpatterns = [
    path('account-view', views.account_view, name = 'account-view'), 
]