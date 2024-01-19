from django.contrib import admin
from .models import Departments,Courses,Materials
# Register your models here.
admin.site.register(Departments)
admin.site.register(Courses)
admin.site.register(Materials)
