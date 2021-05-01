from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    pagenate_by = 
