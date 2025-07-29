# Copyright (C) 2025 Guara - All Rights Reserved
# You may use, distribute and modify this code under the
# terms of the MIT license.
# Visit: https://github.com/douglasdcm/guara


from constants import URL
from transactions import home, setup
from guara.transaction import Application
from guara import it
from wrappers.selenium_wrapper import SeleniumWrapper


class TestTransactionsV2:
    def setup_method(self, method):
        self._app = Application(SeleniumWrapper())
        self._app.at(setup.OpenApp, url=URL)

    def teardown_method(self, method):
        self._app.at(setup.CloseApp)

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
        self._app.at(home.SubmitForm, **with_user_data).asserts(
            it.IsEqualTo, "Form would be submitted here"
        )
