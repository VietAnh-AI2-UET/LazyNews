import requests
from bs4 import BeautifulSoup

def get_html(URL: str) -> BeautifulSoup:
    '''
    Get the HTML presentation of the website

    Argument:
        URL (str): the URL to the news website
    Return:
        soup (BeautifulSoup): DOM tree respresentation of the HTML string
    '''

    response = requests.get(URL)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup