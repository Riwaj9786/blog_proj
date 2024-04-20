from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.PostListView.as_view(), name= 'post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<pk>/edit/', views.UpdatePostView.as_view(), name='post_edit'),
    path('post/<pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
]