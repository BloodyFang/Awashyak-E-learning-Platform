from django.shortcuts import render
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError
from userManagementSystem.models import UserProfileInfo
from django.contrib.auth.decorators import login_required
from userManagementSystem.decorator import login_excluded
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from courseManagementSystem.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

# Render User registration page
@login_excluded('index')
def userRegistration(request):
    return render(request,'register.html')

# User who provide registration information will be store by this method.
def userRegistrationSave(request):
    
    errortype = ""

    if request.method == "GET":
        return render (request,'register.html')

    else:
        try:
            #checks username is unique or not
            if User.objects.filter(username = request.POST.get('userName')).exists():

                errortype = "User Name Already Exist. Please Try Again With Unique User Name."
                raise IntegrityError
                
            #checks email is unique or not
            elif  User.objects.filter(email = request.POST.get('email')).exists():
                
                errortype = "An account With This Email Already Exists."
                raise IntegrityError
                

            else:
                #Gets the data from form fields and store the data into database
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
@login_excluded('index')
def userLogin(request):
    return render(request,'login.html')

# Checks the user credentials is valid or not and redirect to home page.
def loginAuth(request):
    if request.method == "GET":
        return render(request,'login.html')

    else:
        # Check the email and password is valid or not with the help from SettingsBackEnd.py
        # SettingsBackEnd helps to authenticate because default django authentication authenticate by username only
        # In order to authenticate with user we have to build custom SettingsBackEnd.py to authenticate with user email address. 
        auth_user = authenticate(username = request.POST['email'], password= request.POST['password'])

        if auth_user is not None:
            login(request, auth_user)

                
            return redirect('/')

        else:
            messages.error(request,"Invalid username or password.")
            return redirect('login')

# Logout the user and their session
def logoutView(request):
    logout(request)
    return redirect('/')

# login_required is django decorators helps to authenticates users allowed to view which are allowed
# to visit who are authenticated.
@login_required(login_url='login')
def profilePage(request):
    id = request.user.id
    get_user_id = User.objects.get(id = id)
    get_profile_id = UserProfileInfo.objects.get(user_id = id)
    return render(request,'profile.html',{'get_profile_id':get_profile_id, 'get_user_id':get_user_id})

@login_required(login_url='login')
def updateProfilePage(request):
    id = request.user.id
    get_user_id = User.objects.get(id = id)
    get_profile_id = UserProfileInfo.objects.get(user_id = id)
    return render(request,'updateProfile.html',{'get_profile_id':get_profile_id, 'get_user_id':get_user_id})


@login_required(login_url='login')
# updates profile information
def updateProfile(request):

    id = request.user.id
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
                    user.save()

                       
                

                    profile = UserProfileInfo.objects.get(user_id = id)

                    profile.userType = request.POST['update_userType']
                    profile.profilePic = request.FILES.get('profilePic',profile.profilePic)
                        

                

                
                    profile.save()



                   
                    return redirect('profile')

        except IntegrityError:
            messages.info(request, errortype.upper())
            return redirect('update')

# deletes user information form database
def deleteProfile(request):

    get_user_id = request.user.id
    get_user = User.objects.get(id = get_user_id)
    get_user.delete()
    return redirect('index')
        

# changes user password
def changePassword(request):

    if request.method == "GET":
        return render(request,'profile.html')

    else:

        get_id = request.user.id
        user = User.objects.get(id=get_id)

       
        check_password = request.POST.get('check_password')
        update_password = request.POST['update_password']
        check_update_password = request.POST['check_update_password']
        pwd_valid = user.check_password(check_password)


        #pwd_valid = check_password(check_password,user_password)

        if pwd_valid:

            if update_password == check_update_password:
                user.set_password(update_password)
                messages.info(request, 'password changed successfully.You should login again.'.upper() )
                user.save()
                return redirect('update')
            
            else:
                messages.info(request, 'New password and repeat Password did not match.'.upper() )
                return redirect('update')

        else:
            messages.info(request,'Password did not match.Please try again.'.upper())
            return redirect('update')

# render student dashboard       
def studentDashboard(request):
    return render(request, 'studentDashboard.html')

# render teacher dashboard 
def teacherDashboard(request):
    return render(request, 'teacherDashboard.html')


# To see courses that students are enrolled on.
class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])