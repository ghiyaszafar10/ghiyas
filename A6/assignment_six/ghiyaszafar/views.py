from django.shortcuts import render,HttpResponse
from .models import student

# Create your views here.
def studentinfo(request):
    if request.method == 'POST':
        u = str(request.POST['username'])
        e = str(request.POST['staticEmail'])
        p = str(request.POST['inputPassword'])
        p2 = str(request.POST['inputPassword2'])
        f = str(request.POST['firstname'])
        l = str(request.POST['lastname'])

        if p==p2:
            us = student()
            us.username = u
            us.email = e
            us.password = p
            us.first_name = f
            us.last_name = l
            us.save()
            return HttpResponse("Thank you for sign up")
        else:
            return HttpResponse("Your entered password are not match")

    else:
        return render(request,'student_form.html')

