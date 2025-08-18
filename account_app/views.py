from django.shortcuts import render, redirect


from django.contrib.auth import login, authenticate, logout

from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.


# Custom form that takes email and password from the user.
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


# User registration
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




# User login 
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        form.fields['username'].label = "Email" # Change username label to Email
        if form.is_valid():
            email = form.cleaned_data["username"]   # username = email
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
        form.fields['username'].label = "Email" # Change username label to Email
    return render(request, "account_app/login.html", {"form": form})



# User logout
def user_logout(request):
    logout(request)
    return redirect("login")