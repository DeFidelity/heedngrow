from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Q
from .models import Post,Comment,NewsLetter,AboutUs,Tags,Categories,Profile,Contact
from .forms import CommentForm, NewsLetterForm,ContactForm
from django.views.generic import UpdateView,ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages


class IndexView(View):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()[:6]
        tags = Tags.objects.all()
        categories = Categories.objects.all()[:3]

        context = {
            'posts':posts,
            'categories':categories,
            'tags':tags
        }
        return render(request,'blog/index.html',context)

class  BlogList(View):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        categories = Categories.objects.all()



        context={
            'posts':posts,
            'categories':categories
        }
        return render(request,'blog/blog_list.html',context)

class BlogDetail(View):
    def get(self,request,pk,*args,**kwargs):
        post = Post.objects.get(pk=pk)
        comment = Comment.objects.filter(post=post)
        related_posts = Post.objects.all()[:6]

        context={
            'post':post,
            'comments':comment,
            'related_posts':related_posts,
        }
        return render(request,'blog/detail.html',context)
class CommentView(View):
    def post(self,request,pk,*args,**kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request,'Your comment has been added')
            # return redirect('blog_detail',pk=post.pk)
        return render(request,'blog/partials/comment.html',{'form':form,'post':post})
class CommentEditView(UserPassesTestMixin,UpdateView):
    model = Comment
    fields = ['comment']
    template_name = 'social/comment_edit.html'
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post_detail',kwargs={'pk':pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
class CommentReplyView(View):
    def post(self,request, post_pk,pk,*args,**kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.parent = parent_comment
            new_comment.post = post
            new_comment.save()

            context={
                'post':post,
                'comment':parent_comment,
            }

        return render(request,'blog/partials/comment_reply.html',context)


class NewsLetterView(View):
    def post(self,request,*args,**kwargs):
        form= NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thanks for your subscription, you'll receive updates from us weekly")
        return render(request,'blog/partials/newsletter.html',{'form':form})

class ContactTemplate(View):
        def get(self,request,*args,**kwargs):
            return render(request,'blog/contact_filler.html')


class ContactView(View):
    def post(self,request,*args,**kwargs):
        contact = ContactForm(request.POST)
        if contact.is_valid:
            contact.save()
            messages.success(request,"Thanks for contacting us, Our response would get to you soon.")
        return render(request,'blog/partials/contact.html',{'form':contact})

class SearchView(View):
    def get(self,request,*args,**kwargs):
        query = self.request.GET.get('query')

        posts = Post.objects.filter(
            Q(body__icontains=query))

        comments = Comment.objects.filter(
            Q(body__icontains=query)|Q(author__icontains=query))

        categories = Categories.objects.filter(
            Q(category_name__icontains=query)|Q(category_title__icontains=query)|
            Q(category_description__icontains=query)
        )
        profiles = Profile.objects.filter(
            Q(name__icontains=query)|Q(proffession__icontains=query)|
            Q(bio__icontains=query))
        context ={
            'profiles':profiles,
            'posts':posts,
            'comments':comments,
            'categories':categories,
            }

        return render(request,'blog/searches.html',context)


class ExploreTagView(View):
    def get(self,request,*args,**kwargs):
        query = self.request.GET.get('tag_query')
        tag = Tags.objects.filter(tag_name=query).first()
        tags = Tags.objects.all()

        if tags:
            posts = Post.objects.filter(tags__in =[tag])
        context ={
        'query':query,
        'tags':tags,
        'tag':tag,
        'posts':posts,
        }

        return render(request,'blog/tags.html',context)

    def post(self,request,*args,**kwargs):
        explore_form = self.request.POST.get('tag_query')
        if explore_form.is_valid():
            query = explore_form.cleaned_data['tag_query']
            tag = Tags.objects.filter(name=query).first()

            posts = None
            if tag:
                posts = Post.objects.filter(tags__in=[tag])

            if posts:
                context = {
                    'tags':tag,
                    'posts':posts
                }
            else:
                context = {
                    'tags':tag
                }
            return HttpResponseRedirect('/blog/tags?query={query}')
        return HttpResponseRedirect('blog/tags')
class CategoriesListView(ListView):
    context_object_name = 'categories'
    model = Categories
    page_kwarg = 'page'
    paginate_by = 10
    template_name = 'blog/category-list.html'

class CategoryDetailView(View):
    def get(self,request,pk,*args,**kwargs):
        category = Categories.objects.get(pk=pk)
        posts = Post.objects.filter(category=category).all()

        context={
            'category':category,
            'posts':posts,
        }
        return render(request,'blog/category.html',context)

class AboutUsView(View):
    def get(self,request,*args,**kwargs):
        profiles = Profile.objects.all()
        about = AboutUs.objects.all()

        context={
            'about':about,
            'profiles':profiles,
        }
        return render(request,'blog/about.html',context)

class AuthorProfileView(View):
    def get(self,request,pk,*args,**kwargs):
        profile = Profile.objects.get(pk=pk)
        posts = Post.objects.filter(author=profile.user)

        context ={
            'profile':profile,
            'posts':posts,
        }
        return render(request,'blog/profile.html',context)
