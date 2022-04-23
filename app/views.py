from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from app.forms import loginRegister, nurseregister


def image(request):
    return render(request,'admin_temp/admin_home.html')


# Create your views here.
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
               return redirect('admin_home')
            elif user.is_nurse:
                return  redirect('nurse_home')
            elif user.is_user:
                return redirect('user_home')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

def nurse_register(request):
    login_form=loginRegister()
    nurse_form=nurseregister()
    if request.method=='POST':
        login_form=loginRegister(request.POST)
        nurse_form=nurseregister(request.POST)
        if login_form.is_valid() and nurse_form.is_valid():
            user=login_form.save(commit=False)
            user.is_nurse=True
            user.save()
            nurse=nurse_form.save(commit=False)
            nurse.login=login
            nurse.save()
            messages.info(request,'Nurse Registration Successfully')
            return redirect('login_view')

    return render(request,'NurseRegistration.html',{'login_form':login_form,'nurse_form':nurse_form})
