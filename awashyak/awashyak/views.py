from django.shortcuts import render
from django.http import HttpResponse


#render index page
def renderIndexPage(request):
    homePageName={'homePageName':"Awashyak"}
    return render(request,'index.html',context=homePageName)