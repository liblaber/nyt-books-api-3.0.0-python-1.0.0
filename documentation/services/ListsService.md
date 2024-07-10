# ListsService

A list of all methods in the `ListsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                        |
| :-------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| [get_lists_date_list_json](#get_lists_date_list_json)                       | Get Best Sellers list by date.                                     |
| [get_lists_full_overview_format](#get_lists_full_overview_format)           | Get all books for all the Best Sellers lists for specified date.   |
| [get_lists_overview_format](#get_lists_overview_format)                     | Get top 5 books for all the Best Sellers lists for specified date. |
| [get_lists_names_format](#get_lists_names_format)                           | Get Best Sellers list names.                                       |
| [get_lists_best_sellers_history_json](#get_lists_best_sellers_history_json) | Get Best Sellers list history.                                     |

## get_lists_date_list_json

Get Best Sellers list by date.

- HTTP Method: `GET`
- Endpoint: `/lists/{date}/{list}.json`

**Parameters**

| Name   | Type | Required | Description                                                                                                                                                                                  |
| :----- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date\_ | str  | ✅       | YYYY-MM-DD or "current" The date the best sellers list was published on NYTimes.com. Use "current" to get latest list.                                                                       |
| list   | str  | ✅       | Name of the Best Sellers List (e.g. hardcover-fiction). You can get the full list of names from the /lists/names.json service.                                                               |
| offset | int  | ❌       | Sets the starting point of the result set (0, 20, ...). Used to paginate thru books if list has more than 20. Defaults to 0. The num_results field indicates how many books are in the list. |

**Return Type**

`GetListsDateListJsonOkResponse`

**Example Usage Code Snippet**

```python
from nyt_books_sdk import NytBooksSdk, Environment

sdk = NytBooksSdk(
    api_key="",
    base_url=Environment.DEFAULT.value
)

result = sdk.lists.get_lists_date_list_json(
    date_="8521-94-15",
    list="list",
    offset=0
)

print(result)
```

## get_lists_full_overview_format

Get all books for all the Best Sellers lists for specified date.

- HTTP Method: `GET`
- Endpoint: `/lists/full-overview.json`

**Parameters**

| Name           | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :------------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| published_date | str  | ❌       | YYYY-MM-DD The best-seller list publication date. You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26. If you do not include a published date, the current week's best sellers lists will be returned. |

**Return Type**

`OverviewResponse`

**Example Usage Code Snippet**

```python
from nyt_books_sdk import NytBooksSdk, Environment

sdk = NytBooksSdk(
    api_key="",
    base_url=Environment.DEFAULT.value
)

result = sdk.lists.get_lists_full_overview_format(published_date="7545-05-69")

print(result)
```

## get_lists_overview_format

Get top 5 books for all the Best Sellers lists for specified date.

- HTTP Method: `GET`
- Endpoint: `/lists/overview.json`

**Parameters**

| Name           | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :------------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| published_date | str  | ❌       | YYYY-MM-DD The best-seller list publication date. You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26. If you do not include a published date, the current week's best sellers lists will be returned. |

**Return Type**

`OverviewResponse`

**Example Usage Code Snippet**

```python
from nyt_books_sdk import NytBooksSdk, Environment

sdk = NytBooksSdk(
    api_key="",
    base_url=Environment.DEFAULT.value
)

result = sdk.lists.get_lists_overview_format(published_date="3897-02-33")

print(result)
```

## get_lists_names_format

Get Best Sellers list names.

- HTTP Method: `GET`
- Endpoint: `/lists/names.json`

**Return Type**

`GetListsNamesFormatOkResponse`

**Example Usage Code Snippet**

```python
from nyt_books_sdk import NytBooksSdk, Environment

sdk = NytBooksSdk(
    api_key="",
    base_url=Environment.DEFAULT.value
)

result = sdk.lists.get_lists_names_format()

print(result)
```

## get_lists_best_sellers_history_json

Get Best Sellers list history.

- HTTP Method: `GET`
- Endpoint: `/lists/best-sellers/history.json`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                     |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| age_group   | str  | ❌       | The target age group for the best seller.                                                                                                                                                                                                                                                                                                                                       |
| author      | str  | ❌       | The author of the best seller. The author field does not include additional contributors (see Data Structure for more details about the author and contributor fields). When searching the author field, you can specify any combination of first, middle and last names. When sort-by is set to author, the results will be sorted by author's first name.                     |
| contributor | str  | ❌       | The author of the best seller, as well as other contributors such as the illustrator (to search or sort by author name only, use author instead). When searching, you can specify any combination of first, middle and last names of any of the contributors. When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed. |
| isbn        | str  | ❌       | International Standard Book Number, 10 or 13 digits A best seller may have both 10-digit and 13-digit ISBNs, and may have multiple ISBNs of each type. To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229).                                                                                                                     |
| offset      | int  | ❌       | Sets the starting point of the result set (0, 20, ...). Used to paginate thru results if there are more than 20. Defaults to 0. The num_results field indicates how many results there are total.                                                                                                                                                                               |
| price       | str  | ❌       | The publisher's list price of the best seller, including decimal point.                                                                                                                                                                                                                                                                                                         |
| publisher   | str  | ❌       | The standardized name of the publisher                                                                                                                                                                                                                                                                                                                                          |
| title       | str  | ❌       | The title of the best seller When searching, you can specify a portion of a title or a full title.                                                                                                                                                                                                                                                                              |

**Return Type**

`GetListsBestSellersHistoryJsonOkResponse`

**Example Usage Code Snippet**

```python
from nyt_books_sdk import NytBooksSdk, Environment

sdk = NytBooksSdk(
    api_key="",
    base_url=Environment.DEFAULT.value
)

result = sdk.lists.get_lists_best_sellers_history_json(
    age_group="age-group",
    author="author",
    contributor="contributor",
    isbn="isbn",
    offset=0,
    price="price",
    publisher="publisher",
    title="title"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
