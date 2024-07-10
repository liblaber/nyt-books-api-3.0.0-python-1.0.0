# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class BooksBuyLinks2(BaseModel):
    """BooksBuyLinks2

    :param name: name, defaults to None
    :type name: str, optional
    :param url: url, defaults to None
    :type url: str, optional
    """

    def __init__(self, name: str = None, url: str = None):
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url


@JsonMap({})
class ListsBooks(BaseModel):
    """ListsBooks

    :param age_group: age_group, defaults to None
    :type age_group: str, optional
    :param amazon_product_url: amazon_product_url, defaults to None
    :type amazon_product_url: str, optional
    :param article_chapter_link: article_chapter_link, defaults to None
    :type article_chapter_link: str, optional
    :param author: author, defaults to None
    :type author: str, optional
    :param book_image: book_image, defaults to None
    :type book_image: str, optional
    :param book_image_width: book_image_width, defaults to None
    :type book_image_width: int, optional
    :param book_image_height: book_image_height, defaults to None
    :type book_image_height: int, optional
    :param book_review_link: book_review_link, defaults to None
    :type book_review_link: str, optional
    :param book_uri: book_uri, defaults to None
    :type book_uri: str, optional
    :param btrn: btrn, defaults to None
    :type btrn: str, optional
    :param contributor: contributor, defaults to None
    :type contributor: str, optional
    :param contributor_note: contributor_note, defaults to None
    :type contributor_note: str, optional
    :param created_date: created_date, defaults to None
    :type created_date: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param first_chapter_link: first_chapter_link, defaults to None
    :type first_chapter_link: str, optional
    :param price: price, defaults to None
    :type price: str, optional
    :param primary_isbn13: primary_isbn13, defaults to None
    :type primary_isbn13: str, optional
    :param primary_isbn10: primary_isbn10, defaults to None
    :type primary_isbn10: str, optional
    :param publisher: publisher, defaults to None
    :type publisher: str, optional
    :param rank: rank, defaults to None
    :type rank: int, optional
    :param rank_last_week: rank_last_week, defaults to None
    :type rank_last_week: int, optional
    :param sunday_review_link: sunday_review_link, defaults to None
    :type sunday_review_link: str, optional
    :param title: title, defaults to None
    :type title: str, optional
    :param updated_date: updated_date, defaults to None
    :type updated_date: str, optional
    :param weeks_on_list: weeks_on_list, defaults to None
    :type weeks_on_list: int, optional
    :param buy_links: buy_links, defaults to None
    :type buy_links: List[BooksBuyLinks2], optional
    """

    def __init__(
        self,
        age_group: str = None,
        amazon_product_url: str = None,
        article_chapter_link: str = None,
        author: str = None,
        book_image: str = None,
        book_image_width: int = None,
        book_image_height: int = None,
        book_review_link: str = None,
        book_uri: str = None,
        btrn: str = None,
        contributor: str = None,
        contributor_note: str = None,
        created_date: str = None,
        description: str = None,
        first_chapter_link: str = None,
        price: str = None,
        primary_isbn13: str = None,
        primary_isbn10: str = None,
        publisher: str = None,
        rank: int = None,
        rank_last_week: int = None,
        sunday_review_link: str = None,
        title: str = None,
        updated_date: str = None,
        weeks_on_list: int = None,
        buy_links: List[BooksBuyLinks2] = None,
    ):
        if age_group is not None:
            self.age_group = age_group
        if amazon_product_url is not None:
            self.amazon_product_url = amazon_product_url
        if article_chapter_link is not None:
            self.article_chapter_link = article_chapter_link
        if author is not None:
            self.author = author
        if book_image is not None:
            self.book_image = book_image
        if book_image_width is not None:
            self.book_image_width = book_image_width
        if book_image_height is not None:
            self.book_image_height = book_image_height
        if book_review_link is not None:
            self.book_review_link = book_review_link
        if book_uri is not None:
            self.book_uri = book_uri
        if btrn is not None:
            self.btrn = btrn
        if contributor is not None:
            self.contributor = contributor
        if contributor_note is not None:
            self.contributor_note = contributor_note
        if created_date is not None:
            self.created_date = created_date
        if description is not None:
            self.description = description
        if first_chapter_link is not None:
            self.first_chapter_link = first_chapter_link
        if price is not None:
            self.price = price
        if primary_isbn13 is not None:
            self.primary_isbn13 = primary_isbn13
        if primary_isbn10 is not None:
            self.primary_isbn10 = primary_isbn10
        if publisher is not None:
            self.publisher = publisher
        if rank is not None:
            self.rank = rank
        if rank_last_week is not None:
            self.rank_last_week = rank_last_week
        if sunday_review_link is not None:
            self.sunday_review_link = sunday_review_link
        if title is not None:
            self.title = title
        if updated_date is not None:
            self.updated_date = updated_date
        if weeks_on_list is not None:
            self.weeks_on_list = weeks_on_list
        if buy_links is not None:
            self.buy_links = self._define_list(buy_links, BooksBuyLinks2)


@JsonMap({})
class Lists(BaseModel):
    """Lists

    :param list_id: list_id, defaults to None
    :type list_id: int, optional
    :param list_name: list_name, defaults to None
    :type list_name: str, optional
    :param list_name_encoded: list_name_encoded, defaults to None
    :type list_name_encoded: str, optional
    :param display_name: display_name, defaults to None
    :type display_name: str, optional
    :param updated: updated, defaults to None
    :type updated: str, optional
    :param list_image: list_image, defaults to None
    :type list_image: str, optional
    :param list_image_width: list_image_width, defaults to None
    :type list_image_width: int, optional
    :param list_image_height: list_image_height, defaults to None
    :type list_image_height: int, optional
    :param books: books, defaults to None
    :type books: List[ListsBooks], optional
    """

    def __init__(
        self,
        list_id: int = None,
        list_name: str = None,
        list_name_encoded: str = None,
        display_name: str = None,
        updated: str = None,
        list_image: str = None,
        list_image_width: int = None,
        list_image_height: int = None,
        books: List[ListsBooks] = None,
    ):
        if list_id is not None:
            self.list_id = list_id
        if list_name is not None:
            self.list_name = list_name
        if list_name_encoded is not None:
            self.list_name_encoded = list_name_encoded
        if display_name is not None:
            self.display_name = display_name
        if updated is not None:
            self.updated = updated
        if list_image is not None:
            self.list_image = list_image
        if list_image_width is not None:
            self.list_image_width = list_image_width
        if list_image_height is not None:
            self.list_image_height = list_image_height
        if books is not None:
            self.books = self._define_list(books, ListsBooks)


@JsonMap({})
class Result(BaseModel):
    """Result

    :param bestsellers_date: bestsellers_date, defaults to None
    :type bestsellers_date: str, optional
    :param published_date: published_date, defaults to None
    :type published_date: str, optional
    :param published_date_description: published_date_description, defaults to None
    :type published_date_description: str, optional
    :param previous_published_date: previous_published_date, defaults to None
    :type previous_published_date: str, optional
    :param next_published_date: next_published_date, defaults to None
    :type next_published_date: str, optional
    :param lists: lists, defaults to None
    :type lists: List[Lists], optional
    """

    def __init__(
        self,
        bestsellers_date: str = None,
        published_date: str = None,
        published_date_description: str = None,
        previous_published_date: str = None,
        next_published_date: str = None,
        lists: List[Lists] = None,
    ):
        if bestsellers_date is not None:
            self.bestsellers_date = bestsellers_date
        if published_date is not None:
            self.published_date = published_date
        if published_date_description is not None:
            self.published_date_description = published_date_description
        if previous_published_date is not None:
            self.previous_published_date = previous_published_date
        if next_published_date is not None:
            self.next_published_date = next_published_date
        if lists is not None:
            self.lists = self._define_list(lists, Lists)
