from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView, DetailView

from blog.models import Post


class BlogIndex(ListView):
    queryset = Post.objects.all();
    template_name = 'home.html'
    paginate_by = 3

class BlogDetail(DetailView):
        model = Post
        template_name = 'post.html'
