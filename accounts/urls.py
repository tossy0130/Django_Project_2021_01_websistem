from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

# from django.contrib.auth.views import login, logout
from django.contrib.auth.views import(LoginView, LogoutView)
from . import views


app_name ='accounts'


urlpatterns = [

    path('create/', views.Create_account.as_view(), name="create_account"),

    path('',views.Account_login.as_view(),name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),

    ### ユーザー詳細画面
    path('user_detail/<int:pk>/', views.UserDetailView.as_view(), name="user_detail"),

]
