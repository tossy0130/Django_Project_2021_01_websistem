#from kanai_project.kanai_app.forms import LoginForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView, DetailView
from . forms import UserCreateForm

from . forms import UserCreateForm, LoginForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm


############## アカウント作成　用
class Create_account(CreateView):
    
    def post(self, request, *args, **kwargs):
        
        form = UserCreateForm(data=request.POST)

        if form.is_valid():
            form.save()

            # フォームから 'username' を読み取る
            username = form.cleaned_data.get('username')

            # フォームから 'password1' を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('kanai_app:kanri_top')
        return render(request, 'kanai_app/login/create.html', {'form':form})

    def get(self, request, *args, **kwargs):

        form = UserCreateForm(request.POST)
        return render(request, 'kanai_app/login/create.html', {'form':form})


############## ログインフォーム　用
class Account_login(LoginView):
    def post(self, request, *args, **kwargs):
        
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)

            login(request, user)
            return redirect('kanai_app:kanri_top')

        return render(request, 'kanai_app/login/login.html', {'form':form})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'kanai_app/login/login.html', {'form':form})


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'kanai_app/login/login.html'

###################### ユーザー 詳細表示
class UserDetailView(DetailView):

    model = User
    template_name = "kanai_app/login/user_detail.html"
