"""kanai_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#######  追記
from django.conf.urls import include

########## 画像表示用 
from django.conf import settings
from django.conf.urls.static import static # 追加


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('kanai_app/', include('kanai_app.urls')),

    path('summernote/', include('django_summernote.urls')),   # 追記　サマーノート　パス

    path('accounts/', include('accounts.urls')), #追記

    path('calendar/', include('calendar_app.urls')), # 追記　カレンダー

    path('scraping/', include('scraping_app.urls')),

 	path('kanban/', include('kanban.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 追加


