from django.test import TestCase
from django.urls import reverse 
from blog.models import Post, Categories, Comment, Profile,Tags
from django.contrib.auth.models import User

class TestModelMethods(TestCase):
    
    def setUp(self):
        self.author = User.objects.create(
            username='admin',
            password='testpassword'
        )
        
        self.profile = Profile.objects.get(
            user = self.author,
        )
        
        self.category = Categories.objects.create(
            category_name = "new category",
            category_title = "this category is dope",
            category_description = "i like the category"
        )
        
        self.tag = Tags.objects.create(
            tag_name='this tag'
        )
        
        self.blog = Post.objects.create(
            author = self.author,
            title="this is a new post",
            body="this post content is dope for real",
            description='describing this post',
        )
        
        self.second_blog = Post.objects.create(
            author = self.author,
            title="this is a new post by same author",
            body="this post content is dope for real, why not",
            description='describing this post and letting you decide',
        )
        
        self.comment_og = Comment.objects.create(
            post=self.blog,
            author='visitor',
            body="this content",
        )
        
        self.comment_child = Comment.objects.create(
            post=self.blog,
            author='visitor3',
            body="this contentssss",
            parent=self.comment_og
        )
        
        
    def test_post_slugify_method(self):
        self.assertEqual(str(self.blog.slug),'this-is-a-new-post')
        
    def test_post_stringify_method(self):
        self.assertEqual(str(self.blog.title),'this is a new post')
        
    def test_post_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(),reverse('blog_detail',args=[self.blog.slug]))
        
    def test_category_str_method(self):
        self.assertEqual(str(self.category.category_name),"new category")
        
    def test_category_get_absolute_url_method(self):
        self.assertEqual(self.category.get_absolute_url,reverse('category_detail',args=[self.category.category_name]))
        
    def test_tags_str_method(self):
        self.assertEqual(str(self.tag.tag_name),'this tag')
        
    def test_comment_parenting_property(self):
        self.assertEqual(self.comment_og.is_parent,True)
        self.assertEqual(self.comment_og.children.count(),1)
        
    def test_comment_children_property(self):
        self.assertEqual(self.comment_child.is_parent,False)
        self.assertEqual(self.comment_og.children.count(),1)
        
    def test_comment_str_method(self):
        self.assertEqual(str(self.comment_og.author),'visitor')
        
    def test_profile_number_of_post(self):
        self.assertEqual(self.author.profile.num_of_post(self.author),2)
        
    def test_profile_get_absolute_url_method(self):
        self.assertEqual(self.profile.get_absolute_url,reverse('profile',args=[self.author]))
        
    def test_profile_user_posts_method(self):
        self.assertEqual(self.profile.posts(self.author).count(),2)