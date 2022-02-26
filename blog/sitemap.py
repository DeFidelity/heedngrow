from django.contrib.sitemaps import Sitemap

from .models import Post, Categories, Profile

class PostSitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.9
		
		def items(self):
				return Post.objects.all()
		
		def lastmod(self, obj):
				return obj.updated

class CategorySitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.8
		
		def items(self):
				return Categories.objects.all()
		
		def lastmod(self, obj):
				return obj.updated

class ProfileSitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.7
		
		def items(self):
				return Profile.objects.all()
		
		def lastmod(self, obj):
				return obj.updated
