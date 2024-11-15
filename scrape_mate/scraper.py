import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    """Fetches content from the given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.text


def parse_html(html_content, element, class_name=None):
    """Parses the given HTML content and extracts elements."""
    soup = BeautifulSoup(html_content, 'html.parser')
    if class_name:
        return soup.find_all(element, class_=class_name)
    return soup.find_all(element)
