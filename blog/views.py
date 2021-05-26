from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Category, Post
from django.contrib.auth.decorators import login_required

from .forms import CommentForm



def post(request):
    """ Post A Blog """
    posts = Post.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def detail_post(request, slug):
    """ Details on Blog Post """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail_post', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/blog_detail.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)
