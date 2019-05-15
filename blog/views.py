# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import ComentarioForm
from blog.models import Post, Comentario


class BlogIndex(ListView):
    queryset = Post.objects.all();
    template_name = 'home.html'
    paginate_by = 3

class BlogDetail(DetailView):
        model = Post
        template_name = 'post.html'

def comentario_novo(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect (reverse ('post', kwargs={'pk': post.pk}))
    else:
        form = ComentarioForm()
    return render (request, 'comentario.html', {'form': form})

def comentario_like(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.like()
    comentario.save()
    return redirect(reverse ('post', kwargs={'pk': comentario.post_id}))

def comentario_unlike(reques, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.unlike()
    comentario.save()
    return redirect(reverse('post', kwargs={'pk': comentario.post_id}))