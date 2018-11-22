from django.db import models


class WebsiteText(models.Model):
    text = models.CharField(max_length=1000000, blank=True)
    website_url = models.CharField(max_length=250)


class WebsiteImages(models.Model):
    images = models.CharField(max_length=1000000, blank=True)
    website_url = models.CharField(max_length=250)
