# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)

    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# 注册
def register(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            User.objects.create_user(username=username, email='',
                                     password=password)  # 注意 不是 create  因为密码默认是PBKDF2 加密 所以用create  需要手动加密
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render(req, 'register.html', {'uf': uf})


# 登陆
def login_view(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = authenticate(req, username=username, password=password)
            if user:
                # 登录
                login(req, user)
                # 跳转index
                response = HttpResponseRedirect('/user/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                # 比较失败，还在login
                return HttpResponseRedirect('/user/login/')
    else:
        uf = UserForm()
    return render(req, 'login.html', {'uf': uf})


# 登陆成功
@login_required
def index(req):
    username = req.COOKIES.get('username', '')
    return render(req, 'index.html', {'username': username})


# 退出
def logout_view(req):
    response = HttpResponse('logout !!')
    # 清理cookie里保存username
    response.delete_cookie('username')
    # 注销
    logout(req)
    return response
