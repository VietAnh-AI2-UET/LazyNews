from utils import text_utils
from utils import net_utils
from utils import file_utils

class Crawler:
    '''
    A web crawler that fetches and processes website content

    Attributes:
        soup (BeautifulSoup): Parsed HTML of a given URL
        title (str): The title of the given URL
        paragraph (str): Main cleaned text content of the given URL
    '''
    
    def __init__(self, URL):
        '''
        Pass in URL to the website to initiate BeautifulSoup object of the website

        Args:
            URL (str): Link to the website
        '''
        
        self.soup = net_utils.get_html(URL=URL)

    def save_to_txt(self):
        '''
        Save the main content of the website into .txt file
        '''

        file_utils.save_to_txt(self.paragraph)

    def save_to_json(self):
        '''
        Save the main content of the website into .json file
        '''

        file_utils.save_to_json(self.title, self.paragraph)

    def set_title(self):
        '''
        Find the title of the website and set it as this object attribute
        '''

        self.title = self.soup.find('title').get_text(strip=True)
    
    def get_title(self) -> str:
        '''
        Get the title of the website

        Returns:
            title (str): The title of the website
        '''

        return self.title

    def set_paragraph(self):
        '''
        Find the main content of the website, clean it
        and set it as this object attribute
        '''

        paragraphs = self.soup.find_all('p')
        
        # remove tag
        tmp = []    # tag-free input paragraphs
        for p in paragraphs:
            tmp.append(p.get_text(strip=True))

        # get cleaned text
        paragraphs = text_utils.clean_text(paragraphs=tmp)

        # concatenate list[str] into one str
        self.paragraph = ' '.join(paragraphs)

    def get_paragraph(self) -> str:
        '''
        Get the website main content
        
        Returns:
            paragraph (str): Main content of the website
        '''

        return self.paragraph
    
    def get_news(self):
        '''
        Find the title and main content of the website
        and save it to .txt and .json file
        '''
        
        self.set_title()
        self.set_paragraph()
        self.save_to_txt()
        self.save_to_json()