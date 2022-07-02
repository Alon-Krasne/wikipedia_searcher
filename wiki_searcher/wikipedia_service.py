import logging
from typing import List

import wikipedia

from wiki_searcher.models import PageResponse

logger = logging.getLogger(__package__)


def get_wikipedia_page(search_term: str) -> PageResponse:
    logger.debug(f'Searching for {search_term}')
    page = wikipedia.page(search_term, auto_suggest=False)
    logger.debug(f'Got page {page.title}')
    return PageResponse(Title=page.title, Summary=page.summary)


def get_multiple_wiki_pages(disambiguation_options: List[str]) -> List[PageResponse]:
    res = []
    logger.debug('Getting multiple pages: %s', disambiguation_options)
    for option in disambiguation_options:
        res.append(
            get_wikipedia_page(option)
        )
    logger.debug('Got: %d options', len(res))
    return res
