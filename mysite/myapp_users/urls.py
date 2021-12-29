from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name = "myapp_users-register"),    # View to display at localhost:8000/register/
]