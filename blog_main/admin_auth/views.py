from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from .forms import UserEditForm

# Create your views here.
@cache_control(no_cache=True,must_revalidate=True, no_store=True)
def auth_admin(request):
    if request.method=='POST':
        action = request.POST.get('action')
        pk = request.POST.get('user_id')
        user = get_object_or_404(User, pk=pk)
        if action == 'delete':
            if not user.is_superuser:
                user.delete()
            return redirect('admin_auth:admin')
        # elif action == 'edit':
        #     form = UserEditForm(request.POST, instance=user)
        #     if form.is_valid():
        #         form.save()
        #         return redirect('auth_admin:admin')
        #     else:
        #         return render(request, 'edit_user.html', {'form':form, 'user_id':pk})
        
    else:
        if request.user.is_authenticated and request.user.is_superuser:
            user = request.user.username
            users = User.objects.all()
            return render(request, 'admin_auth.html', {'admin_user':user, 'users':users})
        elif request.user.is_authenticated:
            return redirect('blog_homepage:homepage_auth')
        else:
            return redirect('blog_homepage:homepage')
    
def edit_user(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('admin_auth:admin')
        else:
            form = UserEditForm(instance = User)
        return render(request, 'edit_user.html', {'form':form, 'user_id':user_id})
    else:
        form = UserEditForm(instance = user)
        return render(request, 'edit_user.html', {'form':form, 'user_id':user_id})