from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")
]