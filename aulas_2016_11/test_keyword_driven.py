# código do autor
def access_home_page():
    print("Accessing home page")


def navigate_to_flights():
    print("Navigating to flights section")


def source(country, city):
    print(f"Setting source: {city}, {country}")


def destination(country, city):
    print(f"Setting destination: {city}, {country}")


def departure_date(year, mouth, day):
    print(f"Setting departure date: {day}-{mouth}-{year}")


def return_date(year, mouth, day):
    print(f"Setting return date: {day}-{mouth}-{year}")


def search():
    return ["Flight1", "Flight2"]  # Mocked flight results


def test_keyword_driven():
    access_home_page()
    navigate_to_flights()
    source(country="Brazil", city="Belo Horizonte")
    destination(country="Brazil", city="Rio de Janeiro")
    departure_date(year="2024", mouth="may", day="23")
    return_date(year="2024", mouth="may", day="29")
    flights = search()
    assert len(flights) > 0
