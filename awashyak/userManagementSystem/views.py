from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError
from userManagementSystem.models import UserProfileInfo


# Create your views here.

# user registration page

def userRegistration(request):
    return render(request,'register.html')

def userRegistrationSave(request):
    
    errortype = ""

    if request.method == "GET":
        return render (request,'register.html')

    else:
        try:

            if User.objects.filter(username = request.POST.get('userName')).exists():

                errortype = "User Name Already Exist. Please Try Again With Unique User Name."
                raise IntegrityError
                

            elif  UserProfileInfo.objects.filter(email = request.POST.get('email')).exists():
                
                errortype = "An account With This Email Already Exists."
                raise IntegrityError
                

            else:

                user = User (
                first_name = request.POST['firstName'],
                last_name = request.POST['lastName'],
                username = request.POST['userName'],
                password = request.POST['password'],
                )

          
            

                profile = UserProfileInfo (
                    email = request.POST['email'],
                    userType = request.POST['userType'],
                    
                )

            

                user.save()
                profile.save()



                messages.info(request, "Successfully Created Your Account. You Can Login.".upper())
                return redirect('register')

        except IntegrityError:
            messages.info(request, errortype.upper())
            return redirect('register')


# def userRegistration(request):


#     if request.method == "POST":
#         user_form = userRegistrationForm(data= request.POST)
#         profile_form = UserProfileInfoForm(data = request.POST)


#         if user_form.is_valid and profile_form.is_valid:
            
#             user = user_form.save()
#             user.set_password(user_form.cleaned_data['password'])
#             user.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user

#             if 'profile_pic' in request.FILES:
#                 profile.profile_pic = request.FILES['profile_pic']

#             profile.save()

#             return render(request,'register_done.html',{'new_user': user})

#         else:
#             print(user_form.errors,profile_form.errors)
    
#     else:

#         user_form = userRegistrationForm()
#         profile_form = UserProfileInfoForm



#     return render(request,'register.html',
#     {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })




#user login page
def userLogin(request):
    return render(request,'login.html')

    