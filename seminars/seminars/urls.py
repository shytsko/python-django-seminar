"""
URL configuration for seminars project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', include('task2app.urls')),
    path('task5/', include('task5app.urls')),
    path('homework1/', include('homework1.urls')),
    path('seminar3/', include('seminar3.urls')),
    path('seminar4/', include('seminar4.urls')),
    path('homework3/', include('homework3.urls')),
    path('homework4/', include('homework4.urls')),
    path('', include('start_page.urls')),
    path('__debug__/', include("debug_toolbar.urls")),
]
