from bs4 import BeautifulSoup
from bs4.element import Tag
from urllib.parse import urljoin
from utils import net_utils

class NewsFinder:
    '''
    An Agent that searching for recently breaking news

    Attributes:
        _BASE_URL (str): The website where this agent get information from
        _soup (BeautifulSoup): Parsed HTML of a given URL
    '''
    def __init__(self):
        '''
        Initialize NewsFinder object
        '''

        self._BASE_URL = 'https://vietnamnet.vn/'
        self._soup: BeautifulSoup | None = None

    @property
    def BASE_URL(self):
        return self.BASE_URL
    
    @property
    def soup(self):
        raise AttributeError('Direct access to soup is not allowed')

    def _fetch_html(self, URL: str) -> BeautifulSoup:
        '''
        Fetch and return Bs4 object of the website
        '''

        return net_utils.get_html(URL=URL)
    
    def _extract_header_tag(self) -> list[Tag]:
        '''
        Find and extract the <h2> and <h3> tags if availble

        Returns:
            list[Tag]: List of <h2> and <h3>
        '''
        
        if not self._soup:
            return []

        tag_h2 = self._soup.find_all('h2', class_='horizontalPost__main-title vnn-title title-bold')
        tag_h3 = self._soup.find_all('h3', class_='horizontalPost__main-title vnn-title title-bold')

        tag_headers = list(tag_h2) + list(tag_h3)
    
        return tag_headers
        
    def _extract_anchor_tag(self, tag_headers: list[Tag]) -> list[Tag]:
        '''
        Find and extract the <a> tag inside given header tags

        Arguments:
            tag_headers (list[Tag]): List of header tags

        Returns:
            list[Tag]: List of <a> elements
        '''
        
        tag_anchors = []
        for header in tag_headers:
            tag_anchors.append(header.find('a'))
        
        return tag_anchors
    
    def _extract_href(self, tag_anchors: list[Tag]) -> list[str]:
        '''
        Find and extract the 'href' attributes from <a> tags

        Arguments:
            tag_anchors (list[Tag]): List of <a> elements if found

        Returns:
            list[str]: List of href attribute in <a> element if found
        '''
        
        hrefs = []
        for tag_anchor in tag_anchors:
            hrefs.append(tag_anchor['href'])

        return hrefs
    
    def _join_url(self, href: str) -> str:
        '''
        Complete the URL to the website

        Arguments:
            href (str): relative URL to the news

        Returns:
            str: Absolute URL to the news
        '''
        
        return urljoin(base=self._BASE_URL, url=href)
        
    def get_news(self, source='https://vietnamnet.vn/tin-moi-nong'):
        self._soup = self._fetch_html(URL=source)
        tag_header = self._extract_header_tag()
        tag_anchors = self._extract_anchor_tag(tag_headers=tag_header)
        hrefs = self._extract_href(tag_anchors=tag_anchors)

        for i in range(len(hrefs)):
            hrefs[i] = self._join_url(href=hrefs[i])

        return hrefs