import requests

def fetch_content(url):
    """Fetches content from the given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.text
