# Copyright (C) 2025 Guara - All Rights Reserved
# You may use, distribute and modify this code under the
# terms of the MIT license.
# Visit: https://github.com/douglasdcm/guara

from pathlib import Path

from pytest import fixture
from constants import URL
from transactions import home, setup
from guara.transaction import Application
from guara import it

from wrappers.playwright_wrapper import PlaywrightWrapper
from playwright.sync_api import Page

FILE_PATH = Path(__file__).parent.resolve()


class TestTransactionsV3:
    @fixture
    def app(self, page: Page):
        _driver = PlaywrightWrapper(page)

        self._app = Application(_driver)
        self._app.at(
            setup.OpenApp,
            url=URL,
        )
        yield self._app

    def teardown_method(self, method):
        self._app.at(setup.CloseApp)

    def test_aulas(self, app: Application):
        with_user_data = {
            "username": "myname",
            "password": "mypassword",
            "email": "any@any.com",
            "bio": "This is my bio",
            "country": "United Kingdom",
            "age": 30,
            "birthdate": "1993-01-01",  # Adjusted date format for Playwright
        }
        app.at(home.SubmitForm, **with_user_data).asserts(
            it.IsEqualTo, "Form would be submitted here"
        )
