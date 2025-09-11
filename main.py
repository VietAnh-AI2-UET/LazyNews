from utils import net_utils
from utils import file_utils
from core.scraper import crawler
from core.model import summarizer

URLs = ['https://vietnamnet.vn/vu-2-anh-em-bi-danh-nhap-vien-khi-cuu-nguoi-ke-duoc-giup-do-hanh-hung-an-nhan-2441318.html']


soups = [net_utils.get_html(URL=URL) for URL in URLs]
titles = [crawler.get_title(soup=soup) for soup in soups]

print(titles)

# get pages content
paragraphs = [crawler.get_paragraphs(soup=soup) for soup in soups]

# save to txt
file_utils.save_to_txt(paragraphs=paragraphs)

# Read text from .txt file
un_summary_prgs = []
with open('prgs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        un_summary_prgs.append(line.strip())

model, tokenizer = summarizer.get_model()

summary = summarizer.get_summarize(input_text=un_summary_prgs, model=model, tokenizer=tokenizer)
print('Tóm tắt:', summary)