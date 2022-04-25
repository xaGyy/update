from django.urls import path, include
from . import views
from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create', views.create, name='create'),
    path('register/', Register.as_view(), name='register'),
]
