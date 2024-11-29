from selenium.webdriver.common.by import By
from caqui import synchronous, by


class HomePagePlayWright:
    def __init__(self, page):
        self._page = page

    def visit(self):
        self._page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    def fill_input(self, text):
        self._page.locator("id=my-text-id").fill(text)

    def submit_form(self):
        self._page.locator("text=Submit").click()

    def get_submission_message(self):
        return self._page.locator("id=message").text_content()


class HomePageSelenium:
    def __init__(self, page):
        self._page = page

    def visit(self):
        self._page.get("https://www.selenium.dev/selenium/web/web-form.html")

    def fill_input(self, text):
        self._page.find_element(By.ID, "my-text-id").send_keys(text)

    def submit_form(self):
        self._page.find_element(By.CSS_SELECTOR, ".btn").click()

    def get_submission_message(self):
        return self._page.find_element(By.ID, "message").text


class HomePageCaqui:

    def __init__(self, page, session):
        self._page = page
        self._session = session

    def visit(self):
        synchronous.get(
            self._page,
            self._session,
            "https://www.selenium.dev/selenium/web/web-form.html",
        )

    def fill_input(self, text):
        text_box = synchronous.find_element(
            self._page, self._session, by.By.ID, "my-text-id"
        )
        synchronous.send_keys(self._page, self._session, text_box, text)

    def submit_form(self):
        submit_button = synchronous.find_element(
            self._page, self._session, by.By.CSS_SELECTOR, ".btn"
        )
        synchronous.click(self._page, self._session, submit_button)

    def get_submission_message(self):
        message = synchronous.find_element(
            self._page, self._session, by.By.ID, "message"
        )
        return synchronous.get_text(self._page, self._session, message)
