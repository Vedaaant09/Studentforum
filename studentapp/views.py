from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from .models import Contact
# Create your views here.
def index(request):
    if request.method=="POST":
        usn=request.POST.get('usn','')
        name=request.POST.get('name','')
        semester=request.POST.get('semester','')
        phonenumber=request.POST.get('phonenumber','')
        email=request.POST.get('email','')
        if usn and name and semester and email:
            contact=Contact(usn=usn,name=name,semester=semester,phonenumber=phonenumber,email=email)
            contact.save()
        else:
            return HttpResponse("Enter the details")
    return render(request,'welcome.html')