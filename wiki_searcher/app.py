import logging

import pydantic
import wikipedia.exceptions
from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from wiki_searcher.wikipedia_service import get_wikipedia_page

logger = logging.getLogger('wikiSearcher')

app = FastAPI(
    title='ATM API',
    version='0.0.1',
    root_path='/atm/api/v1',
)


class SearchWikiRequest(BaseModel):
    phrase: str
    limit: int

    @pydantic.validator('limit')
    def validate_limit_is_positive(cls, v):
        if v <= 0:
            raise ValueError('Limit must be positive')
        return v


@app.get('/')
async def hello():
    return JSONResponse({'message': 'hello'}, status_code=status.HTTP_200_OK)


@app.get('/search')
async def search_wikipedia(request: SearchWikiRequest = Depends()):
    logger.info(f'Searching for {request.phrase}, with limit {request.limit}')
    try:
        page = get_wikipedia_page(request.phrase)
        return JSONResponse([{'Title': page.title, 'Summary': page.summary}], status_code=status.HTTP_200_OK)
    except wikipedia.exceptions.DisambiguationError as e:
        logger.info('Disambiguation error on page %s', request.phrase)
        pages = e.options
        res = []
        for ind in range(request.limit):
            page = get_wikipedia_page(pages[ind])
            res.append(
                {'Title': page.title, 'Summary': page.summary}
            )
        return JSONResponse(res, status_code=status.HTTP_200_OK)
    except Exception as e:
        logger.exception('Error on page %s', request.phrase)
        return JSONResponse({'error': str(e)}, status_code=status.HTTP_400_BAD_REQUEST)
