from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Welcome to this site</h1> <a href='blog.html'>BLOG</a>")

def blog_page(request):
    return render(request, "myapp/blog.html")