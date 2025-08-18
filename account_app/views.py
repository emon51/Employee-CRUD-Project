from django.shortcuts import render, redirect


from django.contrib.auth import login

from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


# Custom form that takes email and password from the user.
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


# Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data["email"]  
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "account_app/register.html", {"form": form})




