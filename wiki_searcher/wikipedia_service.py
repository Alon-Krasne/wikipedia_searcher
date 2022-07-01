import logging
from typing import List, Optional, Union
import wikipedia
from wikipedia import WikipediaPage

logger = logging.getLogger('wiki_fetcher')


def get_wikipedia_page(search_term: str) -> WikipediaPage:
    return wikipedia.page(search_term)
