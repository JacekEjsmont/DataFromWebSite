from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .test_data import POST_TEXT_DATA, POST_IMAGES_DATA
import json


class TextFromWebsiteTests(APITestCase):
    def test_get_stored_text(self):
        url = reverse('data_from_web_site:scrape_text')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_for_post_text(self):
        url = reverse('data_from_web_site:scrape_text')
        data = {'website_url': 'https://en.wikipedia.org/wiki/Main_Page'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_content_for_post_text(self):
        url = reverse('data_from_web_site:scrape_text')
        data = {'website_url': 'https://www.djangoproject.com/start/overview/'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.content.decode(), json.dumps(POST_TEXT_DATA, separators=(',', ':'), ensure_ascii=False))


class ImagesFromWebsiteTests(APITestCase):
    def test_get_stored_images(self):
        url = reverse('data_from_web_site:scrape_images')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_for_post_images(self):
        url = reverse('data_from_web_site:scrape_images')
        data = {'website_url': 'https://pl.wikipedia.org/wiki/Komputer'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_content_for_post_images(self):
        url = reverse('data_from_web_site:scrape_images')
        data = {'website_url': 'https://pl.wikipedia.org/wiki/Matematyka'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.content.decode(), json.dumps(POST_IMAGES_DATA, separators=(',', ':'), ensure_ascii=False))
