from django.contrib import admin
from .models import (Post,Comment,Categories,
                    Tags,Promotions,NewsLetter,
                    Profile,Contact,AboutUs)


admin.site.site_header = 'Heed n Grow'
admin.site.site_title = 'Heed n Grow'
admin.site.index_title = 'Manage Heed n Grow ...'

class CategoryDisplay(admin.ModelAdmin):
    list_display = ['category_name','category_title','category_description','number_of_posts']
    # list_editable = ['category_name','category_title','category_description']
    empty_value_display = '--empty--'
    exclude = ['created_date']

    def number_of_posts(self,obj):
        n = Post.objects.filter(category=obj)
        posts = len(n.all())
        return posts
    number_of_posts.short_description = "Total Posts"

class NewsLetterDisplay(admin.ModelAdmin):
    list_display = ['email','sign_up_date']
    empty_value_display = '--empty--'

class TagsDisplay(admin.ModelAdmin):
    list_display = ['tag_name','number_of_posts','created_date']
    exclude = ['created_date']
    empty_value_display = '--empty--'


    def number_of_posts(self,obj):
        n = Post.objects.filter(tags=obj)
        posts = len(n.all())
        return posts
    number_of_posts.short_description = "Total Posts"

class PostDisplay(admin.ModelAdmin):
    list_display = ['author','title',]
    list_filter = ('author','category','tags')
    exclude = ['created_date']
    empty_value_display = '--empty--'
    exclude = ['created_date']

class ProfileDisplay(admin.ModelAdmin):
    list_display = ['user','name','bio']


class CommentDisplay(admin.ModelAdmin):
    exclude = ['created_date']
    list_display = ['author','post','body']

class ContactDisplay(admin.ModelAdmin):
    list_display = ['name','email','message','created_date']

admin.site.register(Profile,ProfileDisplay)
admin.site.register(Categories, CategoryDisplay)
admin.site.register(Tags,TagsDisplay)
admin.site.register(Post,PostDisplay)
admin.site.register(Comment,CommentDisplay)
admin.site.register(Promotions)
admin.site.register(NewsLetter,NewsLetterDisplay)
admin.site.register(Contact,ContactDisplay)
admin.site.register(AboutUs)
