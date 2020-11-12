from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
                

            elif  User.objects.filter(email = request.POST.get('email')).exists():
                
                errortype = "An account With This Email Already Exists."
                raise IntegrityError
                

            else:

                user = User.objects.create_user(
                first_name = request.POST['firstName'],
                last_name = request.POST['lastName'],
                username = request.POST['userName'],
                password = request.POST['password'],
                email = request.POST['email'],
                )

                user.save()

                get_username = request.POST['userName']

                get_user_id = User.objects.get(username = get_username)

                save_id = get_user_id.id


            

                profile = UserProfileInfo (
                    
                    userType = request.POST['userType'],
                    user_id = save_id,
                    
                )

            

             
                profile.save()



                messages.info(request, "Successfully Created Your Account. You Can Login.".upper())
                return redirect('register')

        except IntegrityError:
            messages.info(request, errortype.upper())
            return redirect('register')






#user login page
def userLogin(request):
    return render(request,'login.html')


def loginAuth(request):
    if request.method == "GET":
        return render(request,'login.html')

    else:

        auth_user = authenticate(username = request.POST['email'], password= request.POST['password'])

        if auth_user is not None:
            login(request, auth_user)


            return redirect('/')

        else:
            messages.error(request,"Invalid username or password.")
            return redirect('login')

def logoutView(request):
    logout(request)
    return redirect('/')


def profilePage(request,id):
    get_user_id = User.objects.get(id = id)
    get_profile_id = UserProfileInfo.objects.get(user_id = id)
    return render(request,'profile.html',{'get_profile_id':get_profile_id, 'get_user_id':get_user_id})


def updateProfilePage(request,id):
    get_user_id = User.objects.get(id = id)
    get_profile_id = UserProfileInfo.objects.get(user_id = id)
    return render(request,'updateProfile.html',{'get_profile_id':get_profile_id, 'get_user_id':get_user_id})



def updateProfile(request,id):

    errortype = ""

    if request.method == "GET":
        return render (request,'register.html')

    else:
        try:

            if User.objects.filter(username = request.POST.get('update_userName')).exists():

                errortype = "User Name Already Exist. Please Try Again With Unique User Name."
                raise IntegrityError
                

            elif  User.objects.filter(email = request.POST.get('update_email')).exists():
                
                errortype = "An account With This Email Already Exists."
                raise IntegrityError
                

            else:
     
                
                
             

                changeProfile = request.POST.get('updateProfile')
                changePassword = request.POST.get('changePassword')

                if changeProfile == 'updateProfile':
                        
                    user = User.objects.get(id = id)
                    user.first_name = request.POST['update_firstName']
                    user.last_name = request.POST['update_lastName']
                    user.username = request.POST['update_userName']
                    email = request.POST['update_email']
                    user.save()

                       
                

                    profile = UserProfileInfo.objects.get(user_id = id)

                    profile.userType = request.POST['update_userType']
                    profile.profilePic = request.FILES['profilePic']
                        

                

                
                    profile.save()



                    messages.info(request, "Successfully Created Your Account. You Can Login.".upper())
                    return redirect('register')

        except IntegrityError:
            messages.info(request, errortype.upper())
            return redirect('register')

      





    