import requests
from bs4 import BeautifulSoup

def get_html(URL: str) -> BeautifulSoup:
    '''
    Get the HTML presentation of the website

    Args:
        URL (str): the URL to the news website
    
    Returns:
        BeautifulSoup: Parsed HTML of a given URL
    '''

    response = requests.get(URL)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup