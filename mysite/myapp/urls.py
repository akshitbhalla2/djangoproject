from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name = "myapp-home"),                # View to display at localhost:8000
    path("about.html", views.about_page, name = "myapp-about"),    # View to display at localhost:8000/about.html
    path("blog.html", views.blog_page, name = "myapp-blog"),       # View to display at localhost:8000/blog.html
]