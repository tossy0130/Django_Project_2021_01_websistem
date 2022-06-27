from django.urls import path
from .views import Create, listfunc

app_name = 'scraping_app'

urlpatterns = [
    path('', Create.as_view(), name='home'),
    path('list/', listfunc, name='list'),
]
