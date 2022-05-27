"""FinApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from FinancialApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('diary/', views.diary),
    path('profile/', views.profile),
    path('profile/change/', views.change_profile_data),
    path('table/', views.table),
    path('textbook/', views.textbook),
    path('textbook/create/', views.create_article),
    path('textbook/read/<articleID>/', views.read_article),
    path('textbook/exam/<articleID>/', views.pass_exam),
    path('textbook/read/<articleID>/edit/', views.edit_article),
    path('textbook/exam/<articleID>/edit/', views.edit_exam),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)