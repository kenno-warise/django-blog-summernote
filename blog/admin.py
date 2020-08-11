from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    Summernote = '__all__'


admin.site.register(Blog, BlogAdmin)
