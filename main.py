from core.scraper import crawler
from core.model import summarizer

URL = 'https://vietnamnet.vn/my-he-lo-them-hinh-anh-treo-thuong-100-000-usd-tim-ke-am-sat-charlie-kirk-2441707.html'

news = crawler.Crawler(URL=URL)

# get content and save to json
news.get_news()

# Read text from .txt file
un_summary_prgs = []
with open('prgs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        un_summary_prgs.append(line.strip())

sumarization_model = summarizer.Summarizer()

summary = sumarization_model.get_summaries(paragraphs=un_summary_prgs)
print('Tóm tắt:', summary)