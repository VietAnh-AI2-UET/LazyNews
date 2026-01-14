import streamlit as st
from core.model import summarizer
from utils.db_utils import get_news, save_summary


@st.cache_resource
def get_summarizer():
    """Return a cached Summarizer instance (cached across Streamlit sessions).

    Using `@st.cache_resource` ensures the heavy model is created once.
    """
    return summarizer.Summarizer()

def run_summary(data: dict | None = None, save_file: str = 'today_news_summary.json') -> dict:
    """Generate summaries for `data`.

    If `data` is None, read from `today_news.json` (backwards-compatible).
    `data` should be a mapping URL -> {'title': str, 'main_content': str}.
    Returns a mapping URL -> {'title': str, 'summary': str} and saves to `save_file`.
    """

    # read from MongoDB if no data provided
    if data is None:
        data = get_news()

    # initialize (cached) summarizer object
    summary_model = get_summarizer()

    # create a dict for summary paragraphs
    today_news_summary = {}
    for URL, item in data.items():
        # support items that are dicts with 'main_content' and 'title'
        if isinstance(item, dict):
            paragraph = item.get('main_content', '')
            title = item.get('title', '')
        else:
            paragraph = ''
            title = ''

        summary = summary_model.get_summary(paragraph=paragraph) if paragraph else ''
        today_news_summary[URL] = {
            'title': title,
            'summary': summary
        }

    # persist summaries to MongoDB
    save_summary(today_news_summary)
    print("Today news summary saved to MongoDB (collection 'summaries')")

    return today_news_summary