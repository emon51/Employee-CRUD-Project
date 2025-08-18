from django.shortcuts import render, HttpResponse

# Create your views here.

def account_view(request):
    return HttpResponse('This is account view.')

