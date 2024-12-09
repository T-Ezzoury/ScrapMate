"""
scraper.py

This module provides functionalities to fetch and parse HTML content from web pages.
It includes methods to retrieve HTML content from a specified URL and extract
specific HTML elements based on tag names and class attributes.

Dependencies:
- requests
- BeautifulSoup (from bs4)
- logging
"""

import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="web_scraper.log",
    filemode="w",
)


def fetch_content(url):
    """
    Fetches the HTML content from the specified URL.

    Sends an HTTP GET request to the given URL and retrieves the HTML content of the web page.
    Logs the process and handles potential HTTP and request-related errors.

    Args:
        url (str): The URL of the web page to fetch.

    Returns:
        str: The HTML content of the fetched web page.

    Raises:
        requests.exceptions.HTTPError: If an HTTP error occurs (e.g., 4xx or 5xx status codes).
        requests.exceptions.RequestException: For other request-related errors.
    """
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
    """
    Parses HTML content and extracts elements based on tag name and optional class name.

    Utilizes BeautifulSoup to parse the provided HTML content and retrieves all elements
    matching the specified tag. If a class name is provided, it filters elements by the
    given class attribute.

    Args:
        html_content (str): The HTML content to parse.
        element (str): The HTML tag name to search for (e.g., 'div', 'span', 'a').
        class_name (str, optional): The class attribute to filter elements by. Defaults to None.

    Returns:
        list[bs4.element.Tag]: A list of BeautifulSoup Tag objects matching the search criteria.

    Raises:
        Exception: If an error occurs during parsing.
    """
    logging.info("Parsing HTML content")
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        if class_name:
            logging.debug(f"Searching: <{element}> with class '{class_name}'")
            elements = soup.find_all(element, class_=class_name)
        else:
            logging.debug(f"Searching for elements: <{element}> without class")
            elements = soup.find_all(element)

        logging.info(f"Found {len(elements)} elements of type <{element}>")
        return elements
    except Exception as e:
        logging.error(f"Error while parsing HTML content: {e}")
        raise
