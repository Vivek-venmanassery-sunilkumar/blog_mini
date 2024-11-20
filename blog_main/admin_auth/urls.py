from django.urls import path
from . import views

app_name = 'admin_auth'

urlpatterns = [
    path('', views.auth_admin, name = 'admin'),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
]

