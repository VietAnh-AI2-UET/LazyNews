from utils import text_utils, net_utils, file_utils
from bs4 import BeautifulSoup

class Crawler:
    '''
    A web crawler that fetches and processes website content

    Attributes:
        URL (str): Link to the website
        soup (BeautifulSoup): Parsed HTML of a given URL
        title (str): The title of the given URL
        main_content (str): Main cleaned text content of the given URL
    '''

    def __init__(self, URL: str | None = None):
        """
        Initialize the crawler with an optional URL.

        Args:
            URL (str, optional): Website link. Defaults to None.
        """

        self._URL: str | None = None
        self._soup: BeautifulSoup | None = None     #internal
        self._title: str | None = None
        self._main_content: str | None = None

        if URL:
            self.get_news(URL=URL)


    @property
    def url(self) -> str | None:
        '''
        Get the url link to the website
        '''

        return self._URL
    
    @property
    def title(self) -> str | None:
        '''
        Get the title of the website
        '''

        return self._title
    
    @property
    def main_content(self) -> str | None:
        '''
        Get the main content of the website
        '''
        
        return self._main_content
    
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
        
        try:
            tag_title = self._soup.find('title')
            title = tag_title.get_text(strip=True)
            return title
        
        except Exception as e:
            print('Title not exist')
            print(f'Exception: {e}')
            return None
        
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
            print('Nothing in main_content')
            return None
        
        return ' '.join(main_content)
    
    def get_news(self, URL: str) -> None:
        '''
        Search web, find and clean title and main content of the website,
        Set attributes for this object

        Args:
            URL (str): Link to the website
        '''

        self._URL = URL
        self._soup = self._fetch_html(URL=URL)
        self._title = self._extract_title()
        self._main_content = self._extract_main_content()