from rest_framework import serializers
from DataFromWebSiteApp.models import WebsiteText, WebsiteImages


class UrlSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebsiteText
        fields = ['website_url']


class WebSiteTextSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebsiteText
        fields = ['text', 'website_url']


class WebSiteImagesSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebsiteImages
        fields = ['images', 'website_url']
