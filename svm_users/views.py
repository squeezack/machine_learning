from django.shortcuts import render
from django.contrib.auth.models import User

def index (request):
    user = User.objects.all()
    return render(request, 'pages/user/index.html', {'user': user})

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'pages/user/detail.html', {'user': user})