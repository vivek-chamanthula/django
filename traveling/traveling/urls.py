"""
URL configuration for traveling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from travel_explorer import views as turioust #import views from application
from travel_explorer.views import dataview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ab/',turioust.travel), # generate a url      ('creaate_path/',above views.view name from views.py)
    path('tourisum/',turioust.index), # generate a url
    path('view1/',dataview),
]
