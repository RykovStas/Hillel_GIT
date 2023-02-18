# Hillel_GIT HOMEWORK
# <h2>There are 2 functions


* ***First function***
```python
from urllib import parse

def parser(url: str) -> dict:
     params = dict(parse.parse_qsl(parse.urlsplit(url).query))
     return params
```
  This function gets us the query parameters from url


* ***Second function***
```python
def parse_cookie(query: str) -> dict:
    cookies = dict(map(lambda x:x.split('='), query.split(';')))
    return cookies
```
  This function gets us the cookies parameters from string
