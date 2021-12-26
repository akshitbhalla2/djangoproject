from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Akshit Bhalla",
        "title": "Sports",
        "content": "A description of an NBA game",
        "date": "20/12/2021"
    },
    {
        "author": "Tanya Bhalla",
        "title": "Beauty",
        "content": "A tutorial on cosmetic items",
        "date": "12/03/2021"
    },
]

def home_page(request):
    return HttpResponse("<h1>Welcome to this site</h1> <a href='about.html'>ABOUT</a> <br> <a href='blog.html'>BLOG</a>")

def blog_page(request):
    context = {
        "posts": posts,
    }
    return render(request, "myapp/blog.html", context)

def about_page(request):
    context = {
        "title": "About Page",
    }
    return render(request, "myapp/about.html", context)