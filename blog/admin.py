from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'creat_on')
    search_fields = ['name']
    actions = ['approved_comment']

    def approved_comment(self, request, queryset):#Aprove comment in Admin
        queryset.update(approved_comment=True)
  
      
     
admin.site.register(Comment, CommentAdmin)


# Register your models here.
