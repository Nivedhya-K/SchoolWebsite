from django.db import models

# Create your models here.
class Departments(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name=models.CharField(max_length=250)
    departments=models.ForeignKey('Departments',on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Materials(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
