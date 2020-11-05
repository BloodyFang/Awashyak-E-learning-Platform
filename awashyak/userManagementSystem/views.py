from django.shortcuts import render

# Create your views here.

# user registration method
def userRegistration(request):
    return render(request,'register.html')