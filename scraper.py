import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0"
        }

    def fetch_html(self, path=""):
        url = self.base_url + path
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_html(self, html):
        return BeautifulSoup(html, "html.parser")

    def scrape(self, path=""):
        html = self.fetch_html(path)
        if html:
            return self.parse_html(html)
        return None
