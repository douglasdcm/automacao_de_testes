from wrappers.selenium_wrapper import SeleniumWrapper

BASE_URL = "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/"


class TestTransactionsV5:
    def setup_method(self, method):
        self._driver = SeleniumWrapper()

    def teardown_method(self, method):
        self._driver.quit()

    def test_button(self):
        self._driver.goto(f"{BASE_URL}Button.html")
        self._driver.click("home")
        assert (
            self._driver.get_text_by_class_name("wp-heading")
            == "Locators and Selenium Interactions"
        )

    def test_text_input(self):
        self._driver.goto(f"{BASE_URL}Edit.html")
        assert self._driver.get_text("email") == ""
        self._driver.send_text("email", "any@any.com")
        assert self._driver.get_text("email") == "any@any.com"
