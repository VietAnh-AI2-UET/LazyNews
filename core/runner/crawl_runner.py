from core.scraper import crawler, finder
from utils.db_utils import save_news


def run_crawl(save_file: str = 'today_news.json') -> dict:
    """Run the crawler and save results to `save_file`.

    Returns the dictionary of breaking news keyed by URL.
    """
    news_finder = finder.NewsFinder()
    URLs = news_finder.get_news()

    web_crawler = crawler.Crawler()
    breaking_news = {}

    for URL in URLs:
        web_crawler.fetch_html(URL=URL)
        title = web_crawler.get_title()
        main_content = web_crawler.get_main_content()
        if main_content:
            breaking_news[URL] = {
                'title': title,
                'main_content': main_content
            }

    # persist to MongoDB
    save_news(breaking_news)
    print("Today news saved to MongoDB (collection 'news')")
    return breaking_news


if __name__ == '__main__':
    run_crawl()