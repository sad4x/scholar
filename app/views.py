from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import About,Faq,Teacher,Course,Event, Opinion

def main(request):
    context = {
        'abouts':About.objects.all(),
        'faqs':Faq.objects.all(),
        'teachers':Teacher.objects.all(),
        'courses':Course.objects.all(),
        'events':Event.objects.all(),
        'opinions':Opinion.objects.all()
    }
    return render(request, 'index.html', context)

def login_u(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user == None:
            return redirect('/login/')

        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')

def logout_u(request):
    logout(request)
    return redirect('/login/')

def register_u(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username,password=password,is_staff=True)

        return redirect('/login/')

    return render(request,'register.html')