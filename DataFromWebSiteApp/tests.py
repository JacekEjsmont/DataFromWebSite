from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TextFromWebsiteTests(APITestCase):
    def test_get_stored_text(self):
        url = reverse('data_from_web_site:text')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_link_for_text(self):
        url = reverse('data_from_web_site:text')
        data = {'website_url': 'https://en.wikipedia.org/wiki/Main_Page'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ImagesFromWebsiteTests(APITestCase):
    def test_get_stored_text(self):
        url = reverse('data_from_web_site:images')
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_link_for_text(self):
        url = reverse('data_from_web_site:images')
        data = {'website_url': 'https://pl.wikipedia.org/wiki/Komputer'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
