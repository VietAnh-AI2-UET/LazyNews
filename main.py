from utils import file_utils
from core.scraper import crawler
from core.model import summarizer

URL = 'https://vietnamnet.vn/vu-2-anh-em-bi-danh-nhap-vien-khi-cuu-nguoi-ke-duoc-giup-do-hanh-hung-an-nhan-2441318.html'

news = crawler.Crawler(URL=URL)
title = news.get_title()
paragraph = news.get_paragraph()

print(title)

# save to txt
file_utils.save_to_txt(paragraph=paragraph)

# Read text from .txt file
un_summary_prgs = []
with open('prgs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        un_summary_prgs.append(line.strip())

sumarization_model = summarizer.Summarizer()

summary = sumarization_model.get_summarize(input_text=un_summary_prgs)
print('Tóm tắt:', summary)