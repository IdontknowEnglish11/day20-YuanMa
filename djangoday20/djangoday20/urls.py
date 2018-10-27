"""djangoday20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('business/',views.business ),
    path('business_add/',views.login ),
    path('host/',views.host ),
    path('test/',views.test ),
    path('test_ajax/',views.test_ajax ),
    path('dele/',views.dele),
    path('test_edit/',views.test_edit),
    path('app/',views.app),
    path('deleter/',views.deleter),
    path('edit/',views.edit),
]
