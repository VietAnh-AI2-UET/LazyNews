from core.scraper import crawler
from core.model import summarizer
from utils.text_utils import chunk_text

URL = 'https://vietnamnet.vn/dam-phan-nga-ukraine-ban-co-thu-nghiem-cho-trat-tu-the-gioi-2403267.html'

news = crawler.Crawler(URL=URL)

# get content and save to txt and json
news.get_news()

# print title
title = news.get_title()
print(title)

# Read text from .txt file
texts = []
with open('prgs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        texts.append(line)

sumarization_model = summarizer.Summarizer()

summary = sumarization_model.get_summaries(paragraphs=texts)
print('Tóm tắt:')
for s in summary:
    print(s)