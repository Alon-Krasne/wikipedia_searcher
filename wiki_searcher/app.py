import logging
from typing import List

import wikipedia.exceptions
from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse

from wiki_searcher.models import SearchWikiRequest, PageResponse
from wiki_searcher.wikipedia_service import get_wikipedia_page, get_multiple_wiki_pages

logger = logging.getLogger(__package__)

app = FastAPI(
    title='🔍📚 Wikipedia Searcher',
    version='0.0.1',
)


@app.get('/search', response_model=List[PageResponse])
async def search_wikipedia(request: SearchWikiRequest = Depends()):
    logger.debug(f'Searching for {request.phrase}, with limit {request.limit}')
    try:
        res = get_wikipedia_page(request.phrase)
        return JSONResponse([res.dict()], status_code=status.HTTP_200_OK)
    except wikipedia.exceptions.DisambiguationError as e:
        logger.info('Disambiguation error on page %s, getting first %d options', request.phrase, request.limit)
        if e.title != request.phrase:
            logger.warning('No page found on search term %s', request.phrase)
            return JSONResponse([], status_code=status.HTTP_404_NOT_FOUND)
        res = get_multiple_wiki_pages(e.options[:request.limit])
        return JSONResponse([item.dict() for item in res], status_code=status.HTTP_200_OK)
    except Exception:
        logger.exception('Error on page %s, with limit %s', request.phrase, request.limit)
        return JSONResponse({'error': 'Could not process request'}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
