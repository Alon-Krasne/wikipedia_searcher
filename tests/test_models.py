# Test the object creation for all models in models.py
import pytest
from pydantic import ValidationError

from wiki_searcher.models import SearchWikiRequest, PageResponse


def test_create_search_request_success():
    search_request = SearchWikiRequest(phrase='test', limit=10)
    assert search_request.phrase == 'test'
    assert search_request.limit == 10


def test_create_search_request_failure():
    with pytest.raises(ValueError):
        SearchWikiRequest(phrase='test', limit=-1)


def test_create_wiki_page_success():
    page_response = PageResponse(Title='test', Summary='test')
    assert page_response.Title == 'test'
    assert page_response.Summary == 'test'


def test_create_wiki_page_failure():
    with pytest.raises(ValidationError):
        PageResponse(Title='test', Summary=[]) # noqa