from django import forms
from . models import Employee, Department, Achievement



# Department Form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name"]



# Achievement Form
class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ["name"]


# Employee Form
class EmployeeForm(forms.ModelForm):
       
    achievements = forms.ModelMultipleChoiceField(
        queryset=Achievement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False )
       
    class Meta:
        model = Employee
        fields = ["name", "email", "phone", "address", "department", "achievements"]
