from rest_framework import serializers
from DataFromWebSiteApp.models import WebSiteText, WebSiteImages


class UrlSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebSiteText
        fields = ['website_link']


class WebSiteTextSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebSiteText
        fields = ['text', 'website_link']


class WebSiteImagesSerializer(serializers.ModelSerializer):

    class Meta():
        model = WebSiteImages
        fields = ['images', 'website_link']
