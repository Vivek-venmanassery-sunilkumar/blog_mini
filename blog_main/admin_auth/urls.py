from django.urls import path
from . import views

app_name = 'admin_auth'

urlpatterns = [
    path('', views.auth_admin, name = 'admin')
]
