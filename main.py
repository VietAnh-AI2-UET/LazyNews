from core.scraper import crawler
from core.model import summarizer
from utils.text_utils import chunk_text
from utils.file_utils import save_to_json

URLs = ['https://vietnamnet.vn/dam-phan-nga-ukraine-ban-co-thu-nghiem-cho-trat-tu-the-gioi-2403267.html',
       'https://vietnamnet.vn/hoc-tieng-anh-nhu-ngon-ngu-thu-hai-truong-day-ca-van-the-duc-bang-tieng-anh-2444589.html',
       'https://vietnamnet.vn/danh-sach-8-doan-tuyen-cao-toc-duoc-de-nghi-phan-lan-thay-doi-toc-do-xe-chay-2444459.html']

today_news = {}
for URL in URLs:
    news = crawler.Crawler(URL=URL)
    title = news.title
    main_content = news.main_content
    today_news[URL] = {
        'title': title,
        'main_content': main_content 
    }

print(today_news)
save_to_json(today_news)



# # Read text from .txt file
# texts = []
# with open('prgs.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         texts.append(line)

# sumarization_model = summarizer.Summarizer()

# summary = sumarization_model.get_summaries(paragraphs=texts)
# print('Tóm tắt:')
# for s in summary:
#     print(s)