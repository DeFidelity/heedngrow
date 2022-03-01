from urllib import response
from xdrlib import ConversionError
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (IndexView,BlogList,BlogDetail,
                    CommentEditView,NewsLetterView,
                    SearchView,ExploreTagView,CommentView,
                    CategoriesListView,AboutUsView,
                    CategoryDetailView,AuthorProfileView,
                    CommentReplyView,ContactView,ContactTemplate)

class TestURLs(SimpleTestCase):
    
    def test_homepage_url_view_used_and_template(self):
        home_url = reverse('home_page')
        
        response = resolve(home_url)
        
        self.assertEqual(response.func.view_class,IndexView)
        self.assertTemplateUsed('blog/index.html')
        
    def test_bloglist_url_view_used_and_template(self):
        blogs_url = reverse('blog_list')
        
        response = resolve(blogs_url)
        
        self.assertEqual(response.func.view_class,BlogList)
        self.assertTemplateUsed('blog/blog_list.html')
        
    def test_blogdetail_url_view_used_and_template(self):
        
        detail_url = reverse('blog_detail',args=['this-is-a-solid-gee'])
        
        response = resolve(detail_url)
        
        
        self.assertEqual(response.func.view_class,BlogDetail)
        self.assertTemplateUsed('blog/detail.html')
        
    def test_comment_url_view_used_and_template(self):
        
        comment_url = reverse('comments',args=[2])
        response = resolve(comment_url)
        
        self.assertTemplateUsed('blog/partials/comment.html')
        self.assertEqual(response.func.view_class,CommentView)
        
    def test_newsletter_urls(self):
        
        news_url = reverse('newsletter')
        response = resolve(news_url)
        
        self.assertEqual(response.func.view_class,NewsLetterView)
        
    def test_contact_urls_view_class_used(self):
        contact_url = reverse('contact')
        
        response = resolve(contact_url)
        
        self.assertEqual(response.func.view_class,ContactView)
        self.assertTemplateUsed('blog/partials/contact.html')
        
    def test_user_search_urls_for_template_used(self):
        search_url = reverse('search')
        response = resolve(search_url)
        
        self.assertEqual(response.func.view_class,SearchView)
        self.assertTemplateUsed('blog/searches.html')
        
    def test_tag_explore_url_for_view_and_template_used(self):
        tag_url = reverse('tag')
        
        response = resolve(tag_url)
        
        self.assertEqual(response.func.view_class,ExploreTagView)
        self.assertTemplateUsed('blog/tags.html')
        
    def test_category_list_url_view_and_template(self):
        categories = reverse('categories')
        
        response = resolve(categories)
        
        self.assertEqual(response.func.view_class,CategoriesListView)
        self.assertTemplateUsed('blog/category-list.html')
        
    def test_category_detail_url_view_and_template(self):
        
        category = reverse('category_detail',args=['this-category'])
        
        response = resolve(category)
        
        self.assertEqual(response.func.view_class,CategoryDetailView)
        self.assertTemplateUsed('blog/category.html')
        
    def test_about_us_page_url(self):
        
        about_url = reverse('about')
        
        response = resolve(about_url)
        
        self.assertEqual(response.func.view_class,AboutUsView)
        self.assertTemplateUsed('blog/about.html')
        
    def test_user_profile_url(self):
        
        profile_url = reverse('profile',args=['this_user'])
        
        response = resolve(profile_url)
        
        self.assertEqual(response.func.view_class,AuthorProfileView)
        self.assertTemplateUsed('blog/profile.html')
        
        