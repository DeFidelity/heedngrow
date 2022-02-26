from django.contrib import admin
from django.urls import path,include
from blog.sitemap import PostSitemap, CategorySitemap, ProfileSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'posts': PostSitemap,
    'categories': CategorySitemap,
    'profiles': ProfileSitemap,
}


urlpatterns = [
    path('management/',admin.site.urls,name='admin'),
    path('',include('blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
						name='django.contrib.sitemaps.views.sitemap')
]
