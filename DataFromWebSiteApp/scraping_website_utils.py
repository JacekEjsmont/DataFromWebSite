import requests
import re
from bs4 import BeautifulSoup


class ScrapFromWebSite:
    def __init__(self, website_url):
        self.website_url = website_url
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
        """returns text from website in list """
        data = self.soup.findAll(text=True)
        result = list(filter(self.filter_parameter, data))
        return result

    def get_scraped_images(self):
        """return images from website in list"""
        data = self.soup.findAll('img')
        images = []
        for img in data:
            img_link = img.get('src')
            images.append(img_link)
        return images
