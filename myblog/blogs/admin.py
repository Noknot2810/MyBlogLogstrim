from django.contrib import admin

from blogs.models import Blog, Article

admin.site.register(Blog)
admin.site.register(Article)