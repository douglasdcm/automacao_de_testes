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
        # with_user_data = {
        #     "username": "myname",
        #     "password": "mypassword",
        #     "email": "any@any.com",
        #     "bio": "This is my bio",
        #     "country": "United Kingdom",
        #     "age": 30,
        #     "birthdate": "1993-01-01",  # Adjusted date format for Playwright
        # }
        # self._app.at(home.FillForm, **with_user_data).asserts(
        #     it.IsEqualTo, "Form would be submitted here"
        # )
        # self._app.at(home.CheckBoxes)
        self._app.at(home.PushButtons, prompt_text="This is a prompt")
        self._app.at(home.InteractWithDynamicElements).asserts(
            it.HasKeyValue, {"hidden_element": "This element was hidden and now is visible!"}
        ).asserts(it.HasKeyValue, {"new_element": "New element added "}).asserts(
            it.HasKeyValue, {"changed_text": "Text changed at"}
        ).asserts(
            it.HasKeyValue,
            {"toggled_class": "This element will change color when class is toggled"},
        ).asserts(
            it.HasKeyValue, {"ajax_content": "AJAX content loaded at"}
        )
        self._app.at(
            home.SelectDropdowns,
            simple_option="Option 1",
            multi_options=["Green", "Yellow"],
            dynamic_option="Dynamic Option 2",
        )
        result = self._app.at(home.InteractWithTable).result
        assert result["new_row_text"] == "New User 4"
        assert result["original_number_of_rows"] == 3
        assert result["new_number_of_rows"] == 4
        assert result["number_of_rows_after_delete"] == 3
        self._app.at(home.ShowPopover).asserts(it.Contains, "This is a tooltip")
        self._app.at(
            home.UploadFiles,
            file_path="/home/douglas/repo/automacao_de_testes/aulas/docs/email.txt",
            multi_file_path=[
                "/home/douglas/repo/automacao_de_testes/aulas/docs/email.txt",
                "/home/douglas/repo/automacao_de_testes/aulas/docs/UTF8demo.txt",
            ],
        )
        self._app.at(home.InteractWithIFrame).asserts(it.IsEqualTo, "IFrame Content Loaded")
