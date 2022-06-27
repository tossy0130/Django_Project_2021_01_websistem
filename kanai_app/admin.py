from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# Register your models here.

from .models import(Toriatukai_Cate)

class Toriatukai_Cate_admin(admin.ModelAdmin):
        fields = ['Toriatukai_code', 'Toriatukai_title']


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text ')

admin.site.register(Post, PostAdmin)
admin.site.register(Toriatukai_Cate)
