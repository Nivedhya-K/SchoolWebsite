from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import Departments,Courses,Materials

from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('sampleform')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info (request,'Username already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def sampleform(request):
    if request.method == 'POST':
        selected_department_id = request.POST.get('department_id')
        if selected_department_id:
            courses = Courses.objects.filter(departments_id=selected_department_id)
            data = {'courses': [{'id': course.id, 'name': course.name} for course in courses]}
            return JsonResponse(data)
        else:

            data = {'courses': []}
            return JsonResponse(data)
    else:
        departments = Departments.objects.all()
        materials = Materials.objects.all()
        return render(request, 'sampleform.html', {'departments': departments, 'materials': materials})

def submit_form(request):
    purpose = request.POST.get('purpose', '')
    print("Received purpose:", purpose)
    if purpose == 'enquiry':
        message = 'Thank you for your Enquiry!'
    elif purpose == 'placeOrder':
        message = 'Your Order has been Placed Successfully!'
    elif purpose == 'returnOrder':
        message = 'Your Return Order has been Processed!'
    else:
        message = 'Thank you for your submission!'

    return render(request, 'order_confirm.html', {'message': message})


def logout(request):
    auth.logout(request)
    return redirect('/')
