from utils import text_utils, net_utils, file_utils
from bs4 import BeautifulSoup

class Crawler:
    '''
    A web crawler that fetches and processes website content

    Attributes:
        _URL (str): Link to the website
        _soup (BeautifulSoup): Parsed HTML of a given URL
    '''

    def __init__(self, URL: str | None = None):
        """
        Initialize the crawler with an optional URL.

        Args:
            URL (str, optional): Website link. Defaults to None.
        """

        self._URL: str | None = None
        self._soup: BeautifulSoup | None = None     #internal

        if URL:
            self.fetch_html(URL=URL)

    @property
    def URL(self) -> str | None:
        '''
        Get the url link to the website
        '''

        return self._URL
        
    @property
    def soup(self):
        raise AttributeError('Direct access to soup is not allowed')
    
    def _fetch_html(self, URL: str) -> BeautifulSoup:
        '''
        Fetch and return Bs4 object of the website
        '''

        return net_utils.get_html(URL=URL)
    
    def _extract_title(self) -> str | None:
        '''
        Extract website title if available
        '''

        if not self._soup:
            return None
        
        tag_title = self._soup.find('title')
        title = tag_title.get_text(strip=True)
        return title
        
    def _extract_main_content(self) -> str | None:
        '''
        Find and clean main content of the website
        '''

        if not self._soup:
            return None
        
        main_content = []
        tag_paragraphs = self._soup.find_all('p')
        for tag_p in tag_paragraphs:
            p = tag_p.get_text(strip=True)
            if text_utils.is_clean_text(paragraph=p):
                main_content.append(p)

        if not main_content:
            print('This website does not contain any paragraph')
            return None
        
        return '\n'.join(main_content)
    
    def fetch_html(self, URL: str) -> str:
        '''
        Set the _URL and _soup attributes for this object
        
        Args:
            URL (str): Link to the website
        '''

        self._URL = URL
        self._soup = self._fetch_html(URL=self._URL)
    
    def get_title(self) -> str | None:
        '''
        Extract title of the website and return it to user
            
        Returns:
            str | None: Title of the website (if self._soup is availble)'''
        
        title = self._extract_title()
        return title
    
    def get_main_content(self) -> str | None:
        '''
        Extract website main content, clean it, and return it to user

        Returns:
            str | None: Main content of the website (if self._soup is availble)
        '''

        main_content = self._extract_main_content()
        return main_content