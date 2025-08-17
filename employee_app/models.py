from django.db import models

# Create your models here.

#Table Department 
class Department(models.Model):
    #id is default attribute 
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    

#Table Achievement
class Achievement(models.Model):
    #id is default attribute 
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    

#Table Employee
class Employee(models.Model):
    #id is default attribute 
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 15)
    address = models.TextField(blank = True)
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    achievements = models.ManyToManyField(Achievement, through = "AchievementEmployee")
    
    def __str__(self):
        return self.name



#Table AchievementEmployee
class AchievementEmployee(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete = models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    achievement_date = models.DateField()


