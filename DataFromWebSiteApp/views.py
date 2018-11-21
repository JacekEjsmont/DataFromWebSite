import json
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WebSiteText, WebSiteImages
from .serializers import WebSiteTextSerializer, WebSiteImagesSerializer, UrlSerializer
from .scraping_website_utils import ScrapFromWebSite
# Create your views here.


class TextFromWebsiteView(APIView):
    serializer_class = UrlSerializer

    def get(self, request):
        web_site_text = WebSiteText.objects.all()
        serializer = WebSiteTextSerializer(web_site_text, many=True)
        return Response(serializer.data)

    def post(self, request):
        website_url = request.data.get('website_url')

        #Validates given website url
        try:
            requests.get(website_url)
        except ValueError:
            return Response({'Error': 'Can not connect with given url.'
                                      'This website does not exist or you passed url incorrectly'},
                            status=status.HTTP_400_BAD_REQUEST)

        scrapper = ScrapFromWebSite(website_url)
        scraped_text = scrapper.get_scraped_text()

        serializer = WebSiteTextSerializer(data={'website_url': website_url, 'text': json.dumps(scraped_text, ensure_ascii=False)})
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
        website_url = request.data.get('website_url')

        try:
            requests.get(website_url)
        except ValueError:
            return Response({'Error': 'Can not connect with given url. '
                                      'This website does not exist or you passed url incorrectly'},
                            status=status.HTTP_400_BAD_REQUEST)

        scrapper = ScrapFromWebSite(website_url)
        images = scrapper.get_scraped_images()

        serializer = WebSiteImagesSerializer(data={'website_url': website_url, 'images': json.dumps(images, ensure_ascii=False)})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
