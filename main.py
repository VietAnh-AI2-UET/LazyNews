import json
from core.scraper import crawler, finder
from core.model import summarizer
from utils.file_utils import save_to_json

news_finder = finder.NewsFinder()

URLs = news_finder.get_news()

website = crawler.Crawler()
today_news = {}

for URL in URLs:
    website.get_main_content(URL=URL)
    title = website.title
    main_content = website.main_content
    
    if not main_content:
        continue

    today_news[URL] = {
        'title': title,
        'main_content': main_content 
    }

save_to_json(file_name='today_news.json', data=today_news)
print('Today news saved to today_news.json')

# # read from json
# with open('today_news.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# # initialize summarizer object
# summary_model = summarizer.Summarizer()

# # create a dict for summary paragraphs
# today_news_summary = {}
# for URL in URLs:
#     paragraph = data[URL]['main_content']
#     summary = summary_model.get_summary(paragraph=paragraph)
#     today_news_summary[URL] = {
#         'title': today_news[URL]['title'],
#         'summary': summary
#     }

# # save to another .json file
# save_to_json(file_name='today_news_summary.json', data=today_news_summary)
# print('Today news summary saved to today_news_summary.json')