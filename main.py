import json
from core.scraper import crawler, finder
from core.model import summarizer
from utils.file_utils import save_to_json

news_finder = finder.News_finder()

tag_a = news_finder.get_news()

print(tag_a)
print(type(tag_a))







# URLs = ['https://vietnamnet.vn/dam-phan-nga-ukraine-ban-co-thu-nghiem-cho-trat-tu-the-gioi-2403267.html',
#        'https://vietnamnet.vn/hoc-tieng-anh-nhu-ngon-ngu-thu-hai-truong-day-ca-van-the-duc-bang-tieng-anh-2444589.html',
#        'https://vietnamnet.vn/danh-sach-8-doan-tuyen-cao-toc-duoc-de-nghi-phan-lan-thay-doi-toc-do-xe-chay-2444459.html',
#        'https://vnexpress.net/ragasa-giam-duoi-cap-sieu-bao-cach-quang-ninh-570-km-4943022.html']

# website = crawler.Crawler()
# today_news = {}

# for URL in URLs:
#     website.get_news(URL=URL)
#     title = website.title
#     main_content = website.main_content
#     today_news[URL] = {
#         'title': title,
#         'main_content': main_content 
#     }

# save_to_json(file_name='today_news.json', data=today_news)
# print('Today news saved to today_news.json')

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