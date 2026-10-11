from constants import URL
from wrappers.selenium_wrapper import SeleniumWrapper
from pages.form import Form


class TestTransactionsV4:
    def setup_method(self, method):
        self._driver = SeleniumWrapper()
        self._driver.goto(URL)

    def teardown_method(self, method):
        self._driver.quit()

    def test_aulas(self):
        with_user_data = {
            "username": "myname",
            "password": "mypassword",
            "email": "any@any.com",
            "bio": "This is my bio",
            "country": "United Kingdom",
            "age": 30,
            "birthdate": "01-01-1993",
        }
        form = Form(self._driver)
        form.fill_username(with_user_data["username"])
        form.fill_password(with_user_data["password"])
        form.fill_email(with_user_data["email"])
        form.fill_bio(with_user_data["bio"])
        form.select_country(with_user_data["country"])
        form.fill_age(with_user_data["age"])
        form.fill_birthdate(with_user_data["birthdate"])
        assert form.submit() == "Form would be submitted here"
