import wikipedia
from wiki_searcher.wikipedia_service import get_wikipedia_page
from wiki_searcher.utils import configure_logger

logger = configure_logger('wiki_fetcher')

term = "Python_(programming_language)"
page = get_wikipedia_page(term)
page2 = get_wikipedia_page("Python")
print(page)