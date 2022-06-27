from django.urls import path
from . import views
from django.contrib import admin

app_name = 'calendar_app'

urlpatterns = [
     
    path('', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),

    path(
        'month_with_schedule/',
         views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path(
        'month_with_schedule/<int:year>/<int:month>/',
         views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),

    path(
        'month_with_forms/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),

    path(
        'month_with_forms/<int:year>/<int:month>/',
         views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),

]
