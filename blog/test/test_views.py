from django.test import TestCase, Client 
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Categories


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
        
        self.category = Categories.objects.create(
            category_name = "new category",
            category_title = "this category is dope",
            category_description = "i like the category"
        )
        
        self.home_url = reverse('home_page')
        
        self.blog_detail_url = reverse('blog_detail',args=[self.blog.slug])
         
        self.explore_url = reverse('tag')
        
        
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
        
    def test_newsletter_view_with_POST(self):
        newsletter_url = reverse('newsletter')
        
        response = self.client.post(newsletter_url,data={
            'email':'admin@web.com'})
        
        self.assertEqual(response.status_code,200)
        
    def test_search_views_GET(self):
        
        search_url = reverse('search')
        
        response = self.client.get(search_url,data={'query':'find objects'})
 
        self.assertEqual(response.status_code,200)
        
    def test_explore_views_with_GET(self):
        
        response = self.client.get(self.explore_url,data={'tag_query':'world'})
        
        self.assertEqual(response.status_code,200)
        
    def test_explore_views_with_POST(self):
        
        response = self.client.post(self.explore_url,data={'tag_query':'world'})
        
        self.assertEqual(response.status_code,302)
        self.assertTemplateUsed('blog/tags.html')
        
        
    def test_category_list_views_GET(self):
        categories_url = reverse('categories')
        
        response = self.client.get(categories_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('blog/category-list.html')
        
    def test_category_detail_view_get(self):
        
        category_url = reverse('category_detail',args=['new category'])
        
        response = self.client.get(category_url)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('blog/category.html')
        
    def test_about_us_views_GET(self):
        about_url = reverse('about')
        
        response = self.client.get(about_url)
        
        self.assertEqual(response.status_code,200)
        
    def test_author_profile_views_get(self):
        
        author_profile_url = reverse('profile',args=[self.author.pk])
        
        response = self.client.get(author_profile_url)
        
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('blog/profile.html')