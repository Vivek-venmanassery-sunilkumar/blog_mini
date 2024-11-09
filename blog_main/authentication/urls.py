from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('log_in', views.log_in, name='login')
]

