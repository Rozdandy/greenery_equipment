from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Category, Post


def post(request):
    """ Post A Blog """
    posts = Post.objects.all()

    return render(request, template, context)
