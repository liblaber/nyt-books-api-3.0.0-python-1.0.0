# This file was generated by liblab | https://liblab.com/

from nyt_books_sdk import NytBooksSdk, Environment

sdk = NytBooksSdk(api_key="", base_url=Environment.DEFAULT.value)

result = sdk.lists.get_lists_full_overview_format(published_date="7545-05-69")

print(result)