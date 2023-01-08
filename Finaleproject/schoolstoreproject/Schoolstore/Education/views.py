import json
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render, redirect,HttpResponse
from django.template.loader import render_to_string
from .models import Department, Student_Form

def home(request):
    return  render(request,"index.html")

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"Login Successfully")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #      messages.info(request, "Email is already taken")
            #      return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"incorrect password")
            return redirect('register')
        return redirect('/')
           # print("Incorrect Password ")
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('home')
def studentform(request):
    dept = Department.objects.all()
    if request.method  == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        dob = request.POST['dob']
        phonenumber = request.POST['phone']
        gender = request.POST['gender']
        address = request.POST['address']
        mailid = request.POST['email']
        department = request.POST['department']
        course = request.POST['course']
        material = request.POST['material']
        purpose = request.POST['purpose']

        student = Student_Form.objects.create(NAME=name,DOB=dob,AGE=age,PHONE_NUMBER=phonenumber,
                                              GENDER=gender,ADDRESS=address,MAIL_ID=mailid,
                                              DEPARTMENT=dept.get(pk = department),
                                              COURSE=course,MATERIAL=material,PURPOSE=purpose)
        student.save()
        messages.success(request,"Succesfully created.")
        return redirect('studentform')

    context = {
        'dept':dept,
    }
    return render(request, "studentform.html",context)
def course_finder(request):
    dept = request.GET['dept']
    department = Department.objects.filter(id=dept).all()[0]
    #course = department.values_list('courses__course',flat=True)
    #print(department,course)
    print(request.GET['dept'])
    j = render_to_string('courses.html',{'dept': department.courses.all()})
    return JsonResponse({'depart':j})