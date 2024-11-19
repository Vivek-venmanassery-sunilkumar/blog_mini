from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.views.decorators.cache import cache_control
from .forms import SignupForm

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def log_in_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None and user.is_superuser:
            login(request, user)
            request.session['username'] = user.username
            return redirect('admin_auth:admin')
        elif user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('blog_homepage:homepage_auth')
        else:
            return render(request, 'login.html',{'error':'Invalid username or password'})
    else:
        if request.user.is_superuser:
            return redirect('admin_auth:admin')
        elif request.user.is_authenticated:
            return redirect('blog_homepage:homepage_auth')
        else:
            return render(request, 'login.html')

def sign_up_auth(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.first_name = form.cleaned_data['full_name']
            user.save()
            return redirect('authentication:login')
        else:
            return render(request, 'sign_up.html', {'form':form}) 
    else:
        form = SignupForm()
        return render(request, 'sign_up.html', {'form':form})