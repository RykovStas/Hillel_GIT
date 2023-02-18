from urllib import parse

def parser(url: str) -> dict:
    params = dict(parse.parse_qsl(parse.urlsplit(url).query))
    return params



if __name__ == '__main__':
    assert parser('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parser('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parser('http://example.com/') == {}
    assert parser('http://example.com/?') == {}
    assert parser('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parser('https://example.com/path/to/page?name=ferret&color=purple&place=mountains') == {'name': 'ferret', 'color': 'purple', 'place': 'mountains'}
    assert parser('http://example.com/?name==Dima') == {'name': '=Dima'}
    assert parser('http://example.com/?name=Oleg&age=?&') == {'name': 'Oleg', 'age': '?'}
    assert parser('http://example.com/?name=Dima=Admin') == {'name': 'Dima=Admin'}
    assert parser('http://example.com/?name=Dima=Admin&&===None') == {'name': 'Dima=Admin', '': '==None'}
    assert parser('http://example.com/?&?&?&?') == {}
    assert parser('https://example.com/path/to/page?name=ferret?color=purple') == {'name': 'ferret?color=purple'}
    assert parser('http://example.com/&&&&') == {}
    assert parser('http://example.com/????=????') == {'???': '????'}
    assert parser('http://example.com/select&function?') == {}

def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
