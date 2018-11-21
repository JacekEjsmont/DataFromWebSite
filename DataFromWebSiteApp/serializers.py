from rest_framework import serializers
from DataFromWebSiteApp.models import WebSiteText, WebSiteImages


class UrlSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebSiteText
        fields = ['website_url']


class WebSiteTextSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebSiteText
        fields = ['text', 'website_url']


class WebSiteImagesSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebSiteImages
        fields = ['images', 'website_url']
