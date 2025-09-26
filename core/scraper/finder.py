from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime, timedelta
from utils import net_utils

class News_finder:
    '''
    An Agent that searching for recently breaking news

    Attributes:
        soup (BeautifulSoup): Parsed HTML of a given URL
        URLs (list[str]): List of URL to recently breaking news
    '''
    def __init__(self):
        '''
        Initialize News_Finder object
        '''

        self._soup: BeautifulSoup | None = None
        self._URLs: list[str] | None = None

    @property
    def soup(self):
        raise AttributeError('Direct access to soup is not allowed')

    def _fetch_html(self, URL: str ):
        '''
        Fetch and return Bs4 object of the website
        '''

        return net_utils.get_html(URL=URL)
    
    def _extract_header_tag(self) -> list[Tag] | None:
        '''
        Find and extract the <h2> and <h3> elements if availble

        Returns:
            list[Tag] | None: List of <h2> and <h3> elements if found  
        '''
        
        if not self._soup:
            return None
        
        try:
            tag_h2 = self._soup.find_all('h2', class_='horizontalPost__main-title vnn-title title-bold')
            tag_h3 = self._soup.find_all('h3', class_='horizontalPost__main-title vnn-title title-bold')

            tag_headers = list(tag_h2) + list(tag_h3)
        
            return tag_headers
        
        except Exception as e:
            print('No header tag found')
            print(f'Exception" {e}')
        
            return None
        
    def _extract_anchor_tag(self, tag_headers: list[Tag] | None) -> list[Tag] | None:
        '''
        Find and extract the <a> elements if availble

        Arguments:
            tag_headers (list[Tag] | None): List of <h2> and <h3> elements if found

        Returns:
            list[Tag] | None: List of <a> elements if found
        '''
        
        if not tag_headers:
            return None
        
        tag_anchors = []
        for header in tag_headers:
            tag_anchors.append(header.find('a'))
        
        return tag_anchors
    
    def _extract_href(self, tag_anchors: list[Tag] | None) -> list[str] | None:
        '''
        Find and extract the href attributes if availble

        Arguments:
            tag_anchors (list[Tag] | None): List of <a> elements if found

        Returns:
            list[str] | None: List of href attribute in <a> element if found
        '''
        
        hrefs = []
        for tag_anchor in tag_anchors:
            hrefs.append(tag_anchor['href'])

        return hrefs
        
    def get_news(self, source='https://vietnamnet.vn/tin-moi-nong'):
        self._soup = self._fetch_html(URL=source)
        tag_header = self._extract_header_tag()
        tag_anchors = self._extract_anchor_tag(tag_headers=tag_header)
        hrefs = self._extract_href(tag_anchors=tag_anchors)
        return hrefs