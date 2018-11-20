import re
import requests
from bs4 import BeautifulSoup
import json
import nltk

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WebSiteText, WebSiteImages
from .serializers import WebSiteTextSerializer, WebSiteImagesSerializer, UrlSerializer
# Create your views here.


class ScrapFromWebSite:
    def __init__(self, request):
        self.website_url = request.data.get('website_link')
        self.html = requests.get(self.website_url).content
        self.soup = BeautifulSoup(self.html, features='html.parser')

    def filter_parameter(self, element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif element in ['\n', ' ']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True

    def get_scraped_text(self):
        data = self.soup.findAll(text=True)
        result = list(filter(self.filter_parameter, data))
        print(result)
        return result

    def get_scraped_images(self):
        data = self.soup.findAll('img')
        images = []
        for img in data:
            img_link = img.get('src')
            if img_link[:4] == 'http':
                images.append(img_link)
            else:
                images.append('http' + img_link)
        return images


class TextFromWebsiteView(APIView):
    serializer_class = UrlSerializer

    def get(self, request):
        web_site_text = WebSiteText.objects.all()
        serializer = WebSiteTextSerializer(web_site_text, many=True)
        return Response(serializer.data)

    def post(self, request):
        website_data = ScrapFromWebSite(request)
        text = website_data.get_scraped_text()
        website_url = website_data.website_url

        serializer = WebSiteTextSerializer(data=request.data)
        if serializer.is_valid():
            serializer = WebSiteTextSerializer(data={'website_link': website_url, 'text': json.dumps(text)})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesFromWebSiteView(APIView):
    serializer_class = UrlSerializer

    def get(self, request):
        web_site_images = WebSiteImages.objects.all()
        serializer = WebSiteImagesSerializer(web_site_images, many=True)
        return Response(serializer.data)

    def post(self, request):
        website_data = ScrapFromWebSite(request)
        images = website_data.get_scraped_images()
        website_url = website_data.website_url

        serializer = WebSiteImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer = WebSiteImagesSerializer(data={'website_link': website_url, 'images': json.dumps(images)})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
