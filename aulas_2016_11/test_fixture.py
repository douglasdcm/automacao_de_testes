def source(*args, **kwags):
    pass


def destination(*args, **kwags):
    pass


def departure_date(*args, **kwags):
    pass


def return_date(*args, **kwags):
    pass


def search(*args, **kwags):
    return [1]


def test_search():
    source(country="Brazil", city="Belo Horizonte")
    destination(country="Brazil", city="Rio de Janeiro")
    departure_date(year="2024", mouth="may", day="23")
    return_date(year="2024", mouth="may", day="29")
    flights = search()
    assert len(flights) > 0
