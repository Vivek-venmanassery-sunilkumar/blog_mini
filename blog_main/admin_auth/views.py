from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def auth_admin(request):
    if request.method=='POST':
        action = request.POST.get('action')
        if action == 'delete':
            pk = request.POST.get('user_id')
            user = User.objects.get(pk=pk)
            if user.is_superuser:
                print('delete cannot be performed')
            else:
                user.delete()
        elif action == 'edit':
            pk = request.POST.get('user_id')
            user = User.objects.get(pk=pk)
            pass
        return redirect('admin_auth:admin')
    else:
        if request.user.is_authenticated and request.user.is_superuser:
            user = request.user.username
            users = User.objects.all()
            return render(request, 'admin_auth.html', {'admin_user':user, 'users':users})
        elif request.user.is_authenticated:
            return redirect('blog_homepage:homepage_auth')
        else:
            return redirect('blog_homepage:homepage')
    