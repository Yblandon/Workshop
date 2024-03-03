from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss': newss})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.hmtl', {'email':email})