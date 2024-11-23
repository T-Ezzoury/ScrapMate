import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='web_scraper.log',
    filemode='w'
)

def fetch_content(url):
    """Fetches content from the given URL."""
    logging.info(f"Fetching content from URL: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        logging.debug(f"Response status code: {response.status_code}")
        return response.text
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred while fetching URL {url}: {e}")
        raise
    except requests.exceptions.RequestException as e:
        logging.critical(f"Request failed for URL {url}: {e}")
        raise

def parse_html(html_content, element, class_name=None):
    """Parses the given HTML content and extracts elements."""
    logging.info("Parsing HTML content")
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        if class_name:
            logging.debug(f"Searching for elements: <{element}> with class '{class_name}'")
            elements = soup.find_all(element, class_=class_name)
        else:
            logging.debug(f"Searching for elements: <{element}> without specific class")
            elements = soup.find_all(element)
        
        logging.info(f"Found {len(elements)} elements of type <{element}>")
        return elements
    except Exception as e:
        logging.error(f"Error while parsing HTML content: {e}")
        raise
