from django.urls import path
from . import views

app_name = 'blog_homepage'

urlpatterns = [
    path('',views.homepage_main, name='homepage')
]
