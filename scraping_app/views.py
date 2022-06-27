from django.http import response
from django.shortcuts import render
from .models import Scraping
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup
import re

# Create your views here.

class Create(CreateView) :
    
    template_name = 'kanai_app/web_kanri/scraping.html'
    model = Scraping
    fields = ('url',)

    try :
        success_url = reverse_lazy('scraping_app:list')

    except ValueError :

        print("指定された URL から　データを取得できませんでした。")
        

def listfunc(request):
    
    for post in Scraping.objects.all():
        url = post.url
    
    list = []
    response = requests.get(url) #  
    response.encoding = response.apparent_encoding # 文字化け対策
    
    bs = BeautifulSoup(response.text, "html.parser")
    ul_tag = bs.find_all('a')

    try :
        
         # for tag in ul_tag[0]:
          for tag in ul_tag:
            title = tag.text
            url2 = tag.get("href")
            list.append([title, url2])
        
            context = {'list':list}
          return render(request, 'kanai_app/web_kanri/scraping_list.html',context)

    except ValueError :

        print("指定された URL から　データを取得できませんでした。")

    except AttributeError :
        
        print("指定された URL から　データを取得できませんでした。")




  

