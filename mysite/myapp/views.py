from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home_page(request):
    return HttpResponse("<h1>Welcome to this site</h1> <a href='about.html'>ABOUT</a> <br> <a href='blog.html'>BLOG</a>")

def blog_page(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "myapp/blog.html", context)

def about_page(request):
    context = {
        "title": "About Page",
    }
    return render(request, "myapp/about.html", context)