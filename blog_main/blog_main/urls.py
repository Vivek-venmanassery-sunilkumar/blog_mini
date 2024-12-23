from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog_homepage.urls')),
    path('authentication/', include('authentication.urls')),
    path('admin_auth/', include('admin_auth.urls'))
]
