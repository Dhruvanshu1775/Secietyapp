from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib import auth
from django.contrib.auth.models import User
from .models import UserInfo
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from execution.models import HouseNo, Member
from execution.signals import login_success
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user:
            if user.userinfo.is_security:
                dj_login(request, user)
                return redirect('guest')
            if user.userinfo.is_secretary:
                dj_login(request, user)
                return redirect('secretary')
            if user.userinfo.is_member:
                dj_login(request, user)
                return redirect('member')
        else:
            print("no user")

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password']
        id = request.POST['member']
        house = request.POST['house']

        houser_data = HouseNo.objects.get(id = house)

        if not HouseNo.objects.filter(number = houser_data.number, member_id = id):
            return redirect('register')
        else:
            user_obj = User.objects.create_user(username = first_name+last_name, first_name = first_name, last_name = last_name, email = email, password = password1)

            user_info = UserInfo()
            user_info.user_key = user_obj
            user_info.is_member = True
            user_info.save()

            member_obj = Member()
            member_obj.user_key = user_obj
            member_obj.house_key = houser_data
            member_obj.save()
            auth.login(request, user_obj)

            return redirect('member')

        return redirect('register')

    house_obj = HouseNo.objects.all()

    context = {
        'house_obj':house_obj,
    }

    return render(request, 'register.html', context)


def MemberPage(request):
    return render(request, 'member.html')
