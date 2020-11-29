def parse(query: str) -> dict:
    if query == '':
        return {}
        braek
    if query.find('?') == -1:
        return {}
    b = str(query).split('?', 1)[1].split('&')
    if b[-1] == '':
        del b[-1]
    t = 0
    for i in range(len(b)):
        if b[t] == '':
           del b[t] 
           t-= 1
        t+= 1
    d = dict(s.split('=', 1) for s in b)
    return d


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
# 1
    assert parse('https://www.google.com/search?rlz=1C5CHFA_enUA894UA894&sxsrf=ALeKk02R6JovRZvSRzOapN7SNIGCCI3LMA%3A1606652092110&ei=vJDDX-GEBsWWjgb-267YBg&q=%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0+http+&oq=%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0+http+&gs_lcp=CgZwc3ktYWIQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyBggAEBYQHjIGCAAQFhAeMgYIABAWEB5QyF5Y33Rgz3loAHAAeAGAAYEEiAHyLpIBBzMtNC44LjKYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjh0ui53aftAhVFi8MKHf6tC2sQ4dUDCA0&uact=5') == {'rlz': '1C5CHFA_enUA894UA894', 'sxsrf': 'ALeKk02R6JovRZvSRzOapN7SNIGCCI3LMA%3A1606652092110', 'ei': 'vJDDX-GEBsWWjgb-267YBg', 'q': '%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0+http+', 'oq': '%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0+http+', 'gs_lcp': 'CgZwc3ktYWIQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyBggAEBYQHjIGCAAQFhAeMgYIABAWEB5QyF5Y33Rgz3loAHAAeAGAAYEEiAHyLpIBBzMtNC44LjKYAQCgAQGqAQdnd3Mtd2l6wAEB', 'sclient': 'psy-ab', 'ved': '0ahUKEwjh0ui53aftAhVFi8MKHf6tC2sQ4dUDCA0', 'uact': '5'}
# 2
    assert parse('http://shpargalkablog.ru') == {}
# 3
    assert parse('https://www.google.com/search?q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+%D0%B0%D0%BD%D0%B3%D0%BB%D0%BE+-%D1%80%D1%83%D1%81%D1%81&rlz=1C5CHFA_enUA894UA894&oq=&aqs=chrome.0.35i39i362l8...8.232712111j0j15&sourceid=chrome&ie=UTF-8') == {'q': '%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+%D0%B0%D0%BD%D0%B3%D0%BB%D0%BE+-%D1%80%D1%83%D1%81%D1%81', 'rlz': '1C5CHFA_enUA894UA894', 'oq': '', 'aqs': 'chrome.0.35i39i362l8...8.232712111j0j15', 'sourceid': 'chrome', 'ie': 'UTF-8'}
# 4
    assert parse('https://www.google.com/search?name=roma&&age=13') == {'name': 'roma', 'age': '13'}
# 5
    assert parse('https://www.google.com/search?n==j&h=q') == {'n': '=j', 'h': 'q'}
# 6
    assert parse('jwidjd.com') == {}
# 7
    assert parse('https://www.google.com/search??n=j&h=q') == {'?n': 'j', 'h': 'q'}
# 8
    assert parse('https://www.google.com/search?n=j&h?=q') == {'n': 'j', 'h?': 'q'}
# 9
    assert parse('') == {}
# 10
    assert parse('?') == {}

