"""
URL configuration for svm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from svm_login import views as Login
from svm_latih import views as Latih
from svm_dashboard import views as Dashboard
from svm_users import views as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', Dashboard.index, name='dashboard'),
    path('latih/', Latih.index, name='latih'),
    path('classify/', Latih.classify, name='classify'),
    path('', Login.login_view, name='login'),
    path('logout/', Login.logout_view, name='logout'),
    path('users/', users.index, name='users'),
     path('users/<int:pk>/', users.user_detail, name='user_detail'),
     path('latih/<int:pk>/', Latih.data_detail, name='data_detail'),
]
