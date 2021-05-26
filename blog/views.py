from django.shortcuts import render, redirect, reverse, get_object_or_404
from autoslug import AutoSlugField
from .models import Category, Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .forms import PostForm


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


def category(request, slug):
    """ Blog Categories """
    category = Category.objects.get(slug=slug)
    
    template = 'blog/blog_category.html'
    context = {
        'category': category
    }

    return render(request, template, context)


@login_required
def blog_add(request):
    """ Add a blog post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Only Managers can access this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added a post!')
            return redirect(reverse('detail_post', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add post. Please check the form is valid.')
    else:
        form = PostForm()

    template = 'blog/blog_add.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
