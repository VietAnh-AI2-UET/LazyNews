# LazyNews

LazyNews is a Vietnamese news summarization project that collects breaking news from VietnamNet, extracts article content, and generates concise summaries using a pretrained VietAI Transformer model.

## Features

- Collects latest breaking news URLs from `https://vietnamnet.vn/tin-moi-nong`
- Crawls each article and extracts the title and main paragraph text
- Summarizes news content using `VietAI/vit5-base-vietnews-summarization`
- Persists raw news and summary results into MongoDB
- Provides a Streamlit web interface for collection and summarization

## Repository structure

- `app.py` - Main Streamlit app for collecting and summarizing news interactively
- `main.py` - Example script showing how news collection and summarization can be run sequentially
- `core/scraper/finder.py` - Finds recent news article URLs on VietnamNet
- `core/scraper/crawler.py` - Downloads pages and extracts titles and paragraph content
- `core/model/summarizer.py` - Wraps the Hugging Face Transformer summarization model
- `core/runner/crawl_runner.py` - Orchestrates news crawling and saves raw articles
- `core/runner/summary_runner.py` - Orchestrates summarization and saves summaries
- `utils/db_utils.py` - MongoDB persistence utilities for news and summaries
- `utils/net_utils.py` - HTTP fetch helper for retrieving HTML
- `utils/text_utils.py` - Text cleaning and chunking utilities
- `utils/file_utils.py` - JSON/TXT file save helpers

## Requirements

- Python 3.11+ (recommended)
- MongoDB server accessible via `MONGO_URI`
- A working internet connection for web scraping and model downloads

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Configuration

The app uses MongoDB for persistence. By default it connects to `mongodb://localhost:27017`.

To use a custom MongoDB URI, set the environment variable:

```powershell
$env:MONGO_URI = "mongodb://<username>:<password>@<host>:27017"
```

## Run the Streamlit app

From the repository root:

```powershell
python -m streamlit run app.py
```

The app provides buttons for:

- `Thu thập` / `Thu thập lại` - collect raw news from VietnamNet
- `Tóm tắt` / `Tóm tắt lại` - generate summaries for the collected news

## Run the command-line script

The `main.py` script demonstrates a non-interactive pipeline:

```powershell
python main.py
```

This script crawls news and creates `today_news.json` and `today_news_summary.json`.

## Output files

- `today_news.json` - raw article data keyed by URL
- `today_news_summary.json` - summary results keyed by URL

## Notes

- The first run will download the Hugging Face model and may take several minutes.
- The summarizer performs input chunking to handle long articles.
- `today_news.json` and `today_news_summary.json` are included as sample output files.

## Troubleshooting

- If scraping fails, verify the source URL and your internet connection.
- If MongoDB connection fails, ensure `MONGO_URI` is correct and the MongoDB server is running.
- If model loading fails, check that `transformers` and related packages are installed.
