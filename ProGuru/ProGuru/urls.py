"""
URL configuration for ProGuru project.

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
from WebApp import views
from rest_framework.authtoken import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.StudentApi.as_view()),
    path('api-token-auth/', v1.obtain_auth_token),
    path('register/',views.RegisterUser.as_view()),
    path('add/',views.AddStudent,name='add'),
    path('Show/<id>/',views.ShowStudent),

]
