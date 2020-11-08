from django.shortcuts import render

# Create your views here.

# user registration page
def userRegistration(request):
    return render(request,'register.html')

#user login page
def userLogin(request):
    return render(request,'login.html')

    