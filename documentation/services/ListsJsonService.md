# ListsJsonService

A list of all methods in the `ListsJsonService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                                            |
| :------------------------------------ | :--------------------------------------------------------------------- |
| [get_lists_format](#get_lists_format) | Get Best Sellers list. If no date is provided returns the latest list. |

## get_lists_format

Get Best Sellers list. If no date is provided returns the latest list.

- HTTP Method: `GET`
- Endpoint: `/lists.json`

**Parameters**

| Name             | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
| :--------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| list             | str  | ✅       | The name of the Times best sellers list (hardcover-fiction, paperback-nonfiction, ...). The /lists/names service returns all the list names. The encoded list names are lower case with hyphens instead of spaces (e.g. e-book-fiction, instead of E-Book Fiction).                                                                                                                                          |
| bestsellers_date | str  | ❌       | YYYY-MM-DD The week-ending date for the sales reflected on list-name. Times best sellers lists are compiled using available book sale data. The bestsellers-date may be significantly earlier than published-date. For additional information, see the explanation at the bottom of any best-seller list page on NYTimes.com (example: Hardcover Fiction, published Dec. 5 but reflecting sales to Nov. 29). |
| published_date   | str  | ❌       | YYYY-MM-DD The date the best sellers list was published on NYTimes.com (different than bestsellers-date). Use "current" for latest list.                                                                                                                                                                                                                                                                     |
| offset           | int  | ❌       | Sets the starting point of the result set (0, 20, ...). Used to paginate thru books if list has more than 20. Defaults to 0. The num_results field indicates how many books are in the list.                                                                                                                                                                                                                 |

**Return Type**

`GetListsFormatOkResponse`

**Example Usage Code Snippet**

```python
from nyt_books_sdk import NytBooksSdk, Environment

sdk = NytBooksSdk(
    api_key="",
    base_url=Environment.DEFAULT.value
)

result = sdk.lists_json.get_lists_format(
    list="hardcover-fiction",
    bestsellers_date="2872-66-28",
    published_date="3847-84-86",
    offset=0
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->