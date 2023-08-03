"""
URL configuration for anima project.

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
from django.urls import path 
from zoronavi import views
app_name='zoronavi'

urlpatterns = [ 
    path('blog_single', views.blog_single, name='blog_single'),
    path('index', views.index, name='index'),
    path('info', views.info, name='info'),
    path('login_reg', views.login_reg, name='login_reg'),
    path('register', views.register, name='register'),
    path('info', views.info, name='info'),
     ]

