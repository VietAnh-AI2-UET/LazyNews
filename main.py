# this version take 5 minutes to run


import json
from core.scraper import crawler, finder
from core.model import summarizer
from utils.file_utils import save_to_json

news_finder = finder.NewsFinder()

URLs = news_finder.get_news()

web_crawler = crawler.Crawler()
breaking_news = {}

for URL in URLs:
    web_crawler.fetch_html(URL=URL)
    title = web_crawler.get_title()
    main_content = web_crawler.get_main_content()
    # this will fix the 'no content' problem
    if main_content:
        breaking_news[URL] = {
            'title': title,
            'main_content': main_content
        }

# save news to .json file
breaking_news_file = 'today_news.json'
save_to_json(file_name=breaking_news_file, data=breaking_news)
print(f"Today news saved to '{breaking_news_file}'")

# read from json
with open(breaking_news_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# initialize summarizer object
summary_model = summarizer.Summarizer()

# create a dict for summary paragraphs
today_news_summary = {}
for URL in list(data.keys()):
    paragraph = data[URL]['main_content']
    summary = summary_model.get_summary(paragraph=paragraph)
    today_news_summary[URL] = {
        'title': data[URL]['title'],
        'summary': summary
    }

# save to another .json file
summary_file = 'today_news_summary.json'
save_to_json(file_name=summary_file, data=today_news_summary)
print(f"Today news summary saved to '{summary_file}'")