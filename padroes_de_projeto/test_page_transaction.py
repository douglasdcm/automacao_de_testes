# Copyright (C) 2025 Guara - All Rights Reserved
# You may use, distribute and modify this code under the
# terms of the MIT license.
# Visit: https://github.com/douglasdcm/guara

from pathlib import Path
from selenium import webdriver
from transactions import home, contact, info
from guara.transaction import Application
from guara import it, setup

FILE_PATH = Path(__file__).parent.resolve()


class TestVpmTransaction:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        # Comment to show the broken pages
        options.add_argument("--headless")
        self._app = Application(webdriver.Chrome(options=options))
        self._app.at(
            setup.OpenApp,
            url=f"file:///{FILE_PATH}/html/index.html",
        )

    def teardown_method(self, method):
        self._app.at(setup.CloseApp)

    def test_vpm_transaction_chain(self):
        text = "software testing"
        restricted_similariy = "Similarity 10.7%"
        expanded_similarity = "Similarity 15.4%"
        content_in_english = "Content of curriculum"
        content_in_portuguese = "Conteúdo do currículo"

        self._app.at(home.ChangeToPortuguese).asserts(
            it.IsEqualTo, content_in_portuguese
        )
        result = self._app.at(home.ChangeToEnglish).result
        it.IsEqualTo().asserts(result, content_in_english)
        self._app.at(info.NavigateTo).asserts(
            it.Contains,
            (
                "This project was born from the will of its collaborators to help"
                " people to find jobs more easily."
            ),
        )
        self._app.at(home.NavigateTo).asserts(it.IsEqualTo, content_in_english)
        self._app.at(contact.NavigateTo).asserts(
            it.IsEqualTo, "Contact us. We would be happy to answer your questions."
        )
        self._app.at(home.NavigateTo).asserts(it.IsEqualTo, content_in_english)
        self._app.at(
            home.DoRestrictedSearch, text=text, wait_for=restricted_similariy
        ).asserts(it.IsEqualTo, restricted_similariy)
        self._app.at(home.NavigateTo).asserts(it.IsEqualTo, content_in_english)
        self._app.at(
            home.DoExpandedSearch, text=text, wait_for=expanded_similarity
        ).asserts(it.IsEqualTo, expanded_similarity)
        self._app.at(home.NavigateTo).asserts(it.IsEqualTo, content_in_english)
