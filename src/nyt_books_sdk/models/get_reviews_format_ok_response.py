# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class GetReviewsFormatOkResponseResults(BaseModel):
    """GetReviewsFormatOkResponseResults

    :param url: url, defaults to None
    :type url: str, optional
    :param publication_dt: publication_dt, defaults to None
    :type publication_dt: str, optional
    :param byline: byline, defaults to None
    :type byline: str, optional
    :param book_title: book_title, defaults to None
    :type book_title: str, optional
    :param book_author: book_author, defaults to None
    :type book_author: str, optional
    :param summary: summary, defaults to None
    :type summary: str, optional
    :param isbn13: isbn13, defaults to None
    :type isbn13: List[str], optional
    """

    def __init__(
        self,
        url: str = None,
        publication_dt: str = None,
        byline: str = None,
        book_title: str = None,
        book_author: str = None,
        summary: str = None,
        isbn13: List[str] = None,
    ):
        if url is not None:
            self.url = url
        if publication_dt is not None:
            self.publication_dt = publication_dt
        if byline is not None:
            self.byline = byline
        if book_title is not None:
            self.book_title = book_title
        if book_author is not None:
            self.book_author = book_author
        if summary is not None:
            self.summary = summary
        if isbn13 is not None:
            self.isbn13 = isbn13


@JsonMap({})
class GetReviewsFormatOkResponse(BaseModel):
    """GetReviewsFormatOkResponse

    :param status: status, defaults to None
    :type status: str, optional
    :param copyright: copyright, defaults to None
    :type copyright: str, optional
    :param num_results: num_results, defaults to None
    :type num_results: int, optional
    :param results: results, defaults to None
    :type results: List[GetReviewsFormatOkResponseResults], optional
    """

    def __init__(
        self,
        status: str = None,
        copyright: str = None,
        num_results: int = None,
        results: List[GetReviewsFormatOkResponseResults] = None,
    ):
        if status is not None:
            self.status = status
        if copyright is not None:
            self.copyright = copyright
        if num_results is not None:
            self.num_results = num_results
        if results is not None:
            self.results = self._define_list(results, GetReviewsFormatOkResponseResults)