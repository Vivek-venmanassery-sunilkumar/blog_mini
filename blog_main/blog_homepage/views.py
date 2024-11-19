from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def homepage_main(request):
        if request.method == 'POST':
            logout(request)
            request.session.flush()
            return redirect('blog_homepage:homepage')
        else:
            if request.user == None:
                return render(request, 'homepage.html')
            elif request.user.is_authenticated and request.user.is_superuser:
                 return redirect('admin_auth:admin')
            elif request.user.is_authenticated:
                  return redirect('blog_homepage:homepage_auth')
            else:
                  return render(request, 'homepage.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homepage_auth(request):
        if request.user.is_authenticated and request.user.is_superuser:
             return redirect('admin_auth:admin')
        elif request.user.is_authenticated:
            return render(request, 'authenticated_homepage.html')   
        else:
            return redirect('blog_homepage:homepage')