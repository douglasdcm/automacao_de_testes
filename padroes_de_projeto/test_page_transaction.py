from selenium import webdriver
from page_transaction.pages import access, home, contact, info
from page_transaction.transaction import Application


class TestVpmTransaction:
    def setup_method(self, method):
        self._app = Application(webdriver.Chrome())
        self._app.at_page(access.OpenApp)

    def teardown_method(self, method):
        self._app.at_page(access.CloseApp)

    def test_vpm_transaction(self):
        text = "software testing"
        restricted_similariy = "Similarity 10.7%"
        expanded_similarity = "Similarity 15.4%"
        content_in_english = "Content of curriculum"
        content_in_portuguese = "Conteúdo do currículo"

        self._app.at_page(home.ChangeToPortuguese).assert_equals(content_in_portuguese)
        # uses native assertion
        assert self._app.at_page(home.ChangeToEnglish).result == content_in_english
        self._app.at_page(info.GoTo).assert_contains(
            "This project was born from the will of its collaborators to help people to find jobs more easily."
        )
        self._app.at_page(home.GoTo).assert_equals(content_in_english)
        self._app.at_page(contact.GoTo).assert_equals(
            "Contact us. We would be happy to answer your questions."
        )
        self._app.at_page(home.GoTo).assert_equals(content_in_english)
        self._app.at_page(
            home.DoRestrictedSearch, text=text, wait_for=restricted_similariy
        ).assert_equals(restricted_similariy)
        self._app.at_page(home.GoTo).assert_equals(content_in_english)
        self._app.at_page(
            home.DoExpandedSearch, text=text, wait_for=expanded_similarity
        ).assert_equals(expanded_similarity)
        self._app.at_page(home.GoTo).assert_equals(content_in_english)
