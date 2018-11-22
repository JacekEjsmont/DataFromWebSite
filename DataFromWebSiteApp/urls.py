from django.contrib import admin
from django.urls import path, include
from DataFromWebSiteApp import views

urlpatterns = [
    path('scrape_text/', views.TextFromWebsiteView.as_view(), name='scrape_text'),
    path('scrape_images/', views.ImagesFromWebsiteView.as_view(), name='scrape_images')
]
