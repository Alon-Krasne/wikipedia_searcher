from json import JSONEncoder

import pydantic
from pydantic import BaseModel


class SearchWikiRequest(BaseModel):
    phrase: str
    limit: int

    @pydantic.validator('limit')
    def validate_limit_is_positive(cls, v):
        if v <= 0:
            raise ValueError('Limit must be positive')
        return v


class PageResponse(BaseModel):
    Title: str
    Summary: str
