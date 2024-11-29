from playwright.sync_api import sync_playwright
from selenium import webdriver
from caqui import synchronous
from caqui.easy.capabilities import CapabilitiesBuilder, TimeoutsBuilder
from pages import HomePagePlayWright, HomePageSelenium, HomePageCaqui


class TemplateTest:
    def __init__(self):
        raise NotImplementedError

    def run(self):
        self._hp.visit()
        self._hp.fill_input("cheese")
        self._hp.submit_form()
        message = self._hp.get_submission_message()
        assert message == "Received!"


class PlaywrightTest(TemplateTest):
    def __init__(self):
        browser = basic.chromium.launch(headless=False)
        page = browser.new_page()
        self._hp = HomePagePlayWright(page)


class SeleniumTest(TemplateTest):
    def __init__(self):
        self._hp = HomePageSelenium(webdriver.Chrome())


class CaquiTest(TemplateTest):
    def __init__(self):
        self._page = "http://127.0.0.1:9999"
        capabilities = (
            CapabilitiesBuilder()
            .browser_name("chrome")
            .accept_insecure_certs(True)
            .timeouts(TimeoutsBuilder().implicit(1).build())
            # .additional_capability(
            #     {"goog:chromeOptions": {"extensions": [], "args": ["--headless"]}}
            # )
        ).build()
        self._session = synchronous.get_session(self._page, capabilities)
        self._hp = HomePageCaqui(self._page, self._session)


def test_template_caqui():
    c = CaquiTest()
    try:
        c.run()
    finally:
        synchronous.close_session(c._page, c._session)


def test_template_selenium():
    SeleniumTest().run()


with sync_playwright() as basic:
    PlaywrightTest().run()
