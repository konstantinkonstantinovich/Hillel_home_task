def parse_cookie(query: str) -> dict:
    if query == '': return {}
    if query == ';': return {}
    if query == '=': return {}
    a = str(query).split(';')
    if len(a) == 1:
        return {}
    if a[-1] == '':
        del a[-1]
    t = 0
    for i in range(len(a)):
        if a[t] == '':
            del a[t]
            t -= 1
        t += 1
    d = dict(s.split('=', 1) for s in a)
    return d


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
# 1
    assert parse_cookie('name=Dima;;age=28') == {'name': 'Dima', 'age': '28'}
# 2
    assert parse_cookie(';') == {}
# 3
    assert parse_cookie('=') == {}
# 4
    assert parse_cookie('n=r;r=t=y;i=o') == {'n': 'r', 'r': 't=y', 'i': 'o'}
# 5
    assert parse_cookie(';;') == {}
# 6
    assert parse_cookie('a') == {}
# 7
    assert parse_cookie('*') == {}
# 8
    assert parse_cookie('a=a;') == {'a': 'a'}
# 9
    assert parse_cookie('m=n;;;p=r;p=e') == {'m': 'n', 'p': 'r', 'p': 'e'}
# 10
    assert parse_cookie(' ') == {}

