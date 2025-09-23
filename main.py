import json
from core.scraper import crawler
from core.model import summarizer
from utils.file_utils import save_to_json

URLs = ['https://vietnamnet.vn/dam-phan-nga-ukraine-ban-co-thu-nghiem-cho-trat-tu-the-gioi-2403267.html',
       'https://vietnamnet.vn/hoc-tieng-anh-nhu-ngon-ngu-thu-hai-truong-day-ca-van-the-duc-bang-tieng-anh-2444589.html',
       'https://vietnamnet.vn/danh-sach-8-doan-tuyen-cao-toc-duoc-de-nghi-phan-lan-thay-doi-toc-do-xe-chay-2444459.html']

website = crawler.Crawler()
today_news = {}

for URL in URLs:
    website.get_news(URL=URL)
    title = website.title
    main_content = website.main_content
    today_news[URL] = {
        'title': title,
        'main_content': main_content 
    }

save_to_json(file_name='today_news.json', data=today_news)

# read from json
paragraphs = []
with open('today_news.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for url, content in data.items():
    paragraphs.append(content['main_content'])

# initialize summarizer object
summary_model = summarizer.Summarizer()

# feed paragraph into model
summaries = [summary_model.get_summary(paragraph=paragraph) for paragraph in paragraphs]

# create a dict for summary paragraphs
today_news_summary = {}
i = 0
for URL in URLs:
    today_news_summary[URL] = {
        'title': today_news[URL]['title'],
        'summary': summaries[i]
    }
    i += 1

# save to another .json file
save_to_json(file_name='today_news_summary.json', data=today_news_summary)