import logging
from typing import List, Optional, Union
import wikipedia
from wikipedia import WikipediaPage

logger = logging.getLogger('wiki_fetcher')


def get_disambiguation_options(pages: List[str]) -> List[WikipediaPage]:
    res = []
    for page in pages:
        res.append(get_wikipedia_page(page))
    return res


def get_wikipedia_page(search_term: str) -> WikipediaPage:
    return wikipedia.page(search_term)
