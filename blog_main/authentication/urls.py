from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('log_in', views.log_in_auth, name='login'),
    path('sign_up', views.sign_up_auth, name='signup'),
]

