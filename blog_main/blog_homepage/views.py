from django.shortcuts import render

# Create your views here.
def homepage_main(request):
    return render(request, 'homepage.html')