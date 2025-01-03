from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
def aboutus(request):
    return HttpResponse("welcome to the world")
def main(request):
    return HttpResponse("<b>chatrapati shivaji maharaj</b>")
def coursedetail(request,courseid):
    return HttpResponse(courseid)
def home(request):
    return render(request,"index.html.html")
def prod1(request):
    return render(request,"productd.html")
def productd(request):
    return render(request,"prod1.html")
def submitform(request):
     return redirect(features)
    
        
def features(request) :
    return render(request,'features.html')   