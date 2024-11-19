from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def auth_admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        user = request.user.username
        return render(request, 'admin_auth.html', {'admin_user':user})
    elif request.user.is_authenticated:
        return redirect('blog_homepage:homepage_auth')
    else:
        return redirect('blog_homepage:homepage')