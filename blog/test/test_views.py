from django.test import TestCase, Client 
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post
from blog.views import (IndexView,BlogList,BlogDetail,
                    CommentEditView,NewsLetterView,
                    SearchView,ExploreTagView,CommentView,
                    CategoriesListView,AboutUsView,
                    CategoryDetailView,AuthorProfileView,
                    CommentReplyView,ContactView,ContactTemplate)

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        self.author = User.objects.create(
            username='admin',
            password='testpassword'
        )
        
        self.blog = Post.objects.create(
            author = self.author,
            title="this is a new post",
            body="this post content is dope for real",
            description='describing this post',
        )
        
        self.home_url = reverse('home_page')
        self.blog_detail_url = reverse('blog_detail',args=[self.blog.slug])
        
        
    def test_homepage_views_with_GET(self):
        
        
        response = self.client.get(self.home_url)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('blog/index.html')
        
    def test_homepage_views_with_POST(self):
    
        response = self.client.post(self.home_url)
        
        self.assertEqual(response.status_code,405)
        
    def test_bloglist_view_with_GET(self):
        blog_list_url = reverse('blog_list')
        
        response = self.client.get(blog_list_url)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('blog/blog_list.html')
        
    # def test_blog_detail_with_GET(self):
         
    #     response = self.client.get(self.blog_detail_url)
        
    #     self.assertEqual(response.status_code,200)
    #     self.assertTemplateUsed('blog/detail.html')
        
    def test_blog_detail_with_POST(self):
        
        response = self.client.post(self.blog_detail_url)
        
        self.assertEqual(response.status_code,405)
        
    def test_commentviews_with_POST(self):
        comment_url = reverse('comments',args=[self.blog.pk])
        
        response = self.client.post(comment_url,data={
            'author': 'test',
            'body':'comment_body'
            
        })

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('blog/partials/comment.html')