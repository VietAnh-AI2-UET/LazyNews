from utils import text_utils
from utils import net_utils

class Crawler:
    def __init__(self, URL):
        '''
        Pass in URL to the website to initiate BeautifulSoup object of the website
        '''
        self.soup = net_utils.get_html(URL=URL)

    def get_title(self) -> str:
        '''
        Get the title of the website

        Return:
            title (str): The title of the website
        '''

        title = self.soup.find('title').get_text(strip=True)
        return title

    def get_paragraph(self) -> str:
        '''
        Get the main content of the website
        
        Return:
            paragraph (str): Main content of the website
        '''

        paragraphs = self.soup.find_all('p')
        
        # remove tag
        tmp = []    # tag-free input paragraphs
        for p in paragraphs:
            tmp.append(p.get_text(strip=True))

        # get cleaned text
        paragraphs = text_utils.clean_text(paragraphs=tmp)

        # concatenate list[str] into one str
        paragraph = ' '.join(paragraphs)
        return paragraph