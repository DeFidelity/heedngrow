# from django.urls import path
# from .views import (IndexView,BlogList,BlogDetail,
#                     CommentEditView,NewsLetterView,
#                     SearchView,ExploreTagView,CommentView,
#                     CategoriesListView,AboutUsView,
#                     CategoryDetailView,AuthorProfileView,
#                     CommentReplyView,ContactView,ContactTemplate)
# urlpatterns=[
#     path('',IndexView.as_view(),name='home_page'),
#     path('blogs/all/',BlogList.as_view(),name='blog_list'),
#     path('blog/detail/<int:pk>/',BlogDetail.as_view(),name='blog_detail'),
#     path('blog/<int:pk>/comment/',CommentView.as_view(),name='comments'),
#     path('blog/<int:pk>/comment/edit/',CommentEditView.as_view(),name='comment_edit'),
#     path('p/<int:post_pk>/comment/<int:pk>reply/',CommentReplyView.as_view(),name='comment_reply'),
#     path('newsleter/',NewsLetterView.as_view(),name='newsletter'),
#     path('contact',ContactView.as_view(),name='contact'),
#     path('contact/home/',ContactTemplate.as_view(),name='contact_template'),
#     path('search/',SearchView.as_view(),name='search'),
#     path('explore/tags/',ExploreTagView.as_view(),name='tag'),
#     path('categories/all/',CategoriesListView.as_view(),name='categories'),
#     path('category/<str:pk>/',CategoryDetailView.as_view(),name='category_detail'),
#     path('about-us/',AboutUsView.as_view(),name='about'),
#     path('profile/<str:pk>/',AuthorProfileView.as_view(),name='profile')
# ]
