from enum import unique
from tkinter import N
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from autoslug import AutoSlugField
from django.dispatch import receiver


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(blank=True,default=timezone.now)
    body = RichTextField()
    category = models.ManyToManyField('Categories',blank=True,null=True)
    image = models.ImageField(upload_to='media/posts/',null=True)
    tags = models.ManyToManyField('Tags',blank=False,related_name='tags')
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    slug = AutoSlugField(populate_from='title',default="okayys")

    class Meta:
        ordering =['-created_date']

    def __str__(self):
        return self.title
    
    
class Categories(models.Model):
    category_name = models.CharField(max_length=150,primary_key=True)
    category_title = models.CharField(max_length=150)
    category_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    category_image = models.ImageField(upload_to='media/category/',null=True)
    slug = AutoSlugField(populate_from='category_name',default="this_one")

    class Meta:
        ordering =['created_date']

    def __str__(self):
        return self.category_name

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(populate_from='tag_name',default="this_tag")

    def __str__(self):
        return self.tag_name

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=40)
    body = models.TextField()
    tags = models.ManyToManyField('Tags',related_name='comment_tags',)
    avi = models.ImageField(upload_to='media/profile/',null=True)
    created_date = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='+')

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('created_date').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    class Meta:
        ordering =['-created_date']

    def __str__(self):
        return self.author

class Promotions(models.Model):
    main = models.CharField(max_length=400)
    main_text = RichTextField()

class NewsLetter(models.Model):
    email = models.EmailField()
    sign_up_date = models.DateTimeField(default=timezone.now)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user',related_name='profile',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    avi = models.ImageField(upload_to="media/profile/",null=True)
    proffession = models.CharField(max_length=150,null=True,blank=True,default='Writter')
    bio = models.CharField(max_length=300, null=True,blank=True)

    def num_of_post(self,user):
        posts = Post.objects.filter(author=user).all()
        n = len(posts)
        return n

    def posts(self,user):
        posts = Post.objects.filter(author=user).all()
        return posts

    def __str__(self):
        return str(self.user)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

class AboutUs(models.Model):
    about_intro = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.about_intro)

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance,**kwargs):
    instance.profile.save()
