from django.contrib import admin
from django.urls import path, include
from DataFromWebSiteApp import views

urlpatterns = [
    path('text/', views.TextFromWebsiteView.as_view(), name='text'),
    path('images/', views.ImagesFromWebsiteView.as_view(), name='images')
]
