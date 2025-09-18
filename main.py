from core.scraper import crawler
from core.model import summarizer
from utils.text_utils import chunk_text

URL = 'https://vietnamnet.vn/trung-quoc-phan-ung-truoc-tuyen-bo-cua-my-lien-quan-toi-xung-dot-nga-ukraine-2442829.html'

news = crawler.Crawler(URL=URL)

# get content and save to txt and json
news.get_news()

# print title
title = news.get_title()
print(title)

# Read text from .txt file
with open('prgs.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sumarization_model = summarizer.Summarizer()

summary = sumarization_model.get_summaries(paragraph=text)
print('Tóm tắt:')
for s in summary:
    print(s + '\n')