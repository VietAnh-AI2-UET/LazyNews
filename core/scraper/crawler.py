from bs4 import BeautifulSoup
from utils import text_utils

def get_title(soup: BeautifulSoup) -> str:
    '''
    Get the titile of the website

    Argument:
        soup (BeautifulSoup): DOM tree: respresentation of the HTML string
    Return:
        title (str): The title of the website
    '''

    title = soup.find('title').get_text(strip=True)
    return title

def get_paragraphs(soup: BeautifulSoup) -> str:
    '''
    Get the main content of the website
    
    Arguments:
        soup (BeautifulSoup): DOM tree: respresentation of the HTML string
    Return:
        paragraphs (str): Main content of the website
    '''

    paragraphs = soup.find_all('p')
    
    # remove tag
    tmp = []    # tag-free input paragraphs
    for p in paragraphs:
        tmp.append(p.get_text(strip=True))

    # get cleaned text
    paragraphs = text_utils.clean_text(paragraphs=tmp)

    # concatenate list[str] into one str
    paragraphs = ' '.join(paragraphs)
    return paragraphs