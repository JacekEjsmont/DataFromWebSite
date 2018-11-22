import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WebsiteText, WebsiteImages
from .serializers import WebsiteTextSerializer, WebsiteImagesSerializer, UrlSerializer
from .scraping_website_utils import ScrapFromWebsite
# Create your views here.


class TextFromWebsiteView(APIView):
    serializer_class = UrlSerializer

    def get(self, request):
        web_site_text = WebsiteText.objects.all()
        serializer = WebsiteTextSerializer(web_site_text, many=True)
        return Response(serializer.data)

    def post(self, request):
        website_url = request.data.get('website_url')

        #Validates given website url
        try:
            requests.get(website_url)
        except ValueError:
            return Response({'Error': 'Can not connect with given url.'
                                      'This website does not exist or you have passed url incorrectly'},
                            status=status.HTTP_400_BAD_REQUEST)

        #Validates if text is in database
        if WebsiteText.objects.filter(website_url=website_url):
            return Response({'Error': 'Text already in database'}, status=status.HTTP_400_BAD_REQUEST)

        scrapper = ScrapFromWebsite(website_url)
        scraped_text = scrapper.get_scraped_text()

        serializer = WebsiteTextSerializer(data={'website_url': website_url, 'text': json.dumps(scraped_text, ensure_ascii=False)})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesFromWebsiteView(APIView):
    serializer_class = UrlSerializer

    def get(self, request):
        web_site_images = WebsiteImages.objects.all()
        serializer = WebsiteImagesSerializer(web_site_images, many=True)
        return Response(serializer.data)

    def post(self, request):
        website_url = request.data.get('website_url')

        # Validates given website url
        try:
            requests.get(website_url)
        except ValueError:
            return Response({'Error': 'Can not connect with given url. '
                                      'This website does not exist or you have passed url incorrectly'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Validates if images are in database
        if WebsiteImages.objects.filter(website_url=website_url):
            return Response({'Error': 'Images already in database'}, status=status.HTTP_400_BAD_REQUEST)

        scrapper = ScrapFromWebsite(website_url)
        images = scrapper.get_scraped_images()

        serializer = WebsiteImagesSerializer(data={'website_url': website_url, 'images': json.dumps(images, ensure_ascii=False)})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
