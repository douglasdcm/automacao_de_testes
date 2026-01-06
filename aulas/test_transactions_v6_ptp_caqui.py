# Copyright (C) 2025 Guara - All Rights Reserved
# You may use, distribute and modify this code under the
# terms of the MIT license.
# Visit: https://github.com/douglasdcm/guara

import os
from constants import URL
from transactions import home, setup
from guara.transaction import Application
from guara import it
from wrappers.caqui_wrapper import CaquiWrapper
from caqui.easy.server import Server
from time import sleep
from constants import URL

SERVER_PORT = 9999
SERVER_URL = f"http://localhost:{SERVER_PORT}"
CURRENT_DIR = os.getcwd()


class TestTransactionsV6:
    def setup_method(self, method):
        self._server = Server.get_instance(port=SERVER_PORT)
        self._server.start()

        driver = CaquiWrapper(server_url=SERVER_URL)
        self._app = Application(driver)
        self._app.at(setup.OpenApp, url=URL)

    def teardown_method(self, method):
        self._app.at(setup.CloseApp)
        # sleep(3)
        # self._server.dispose()

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
        self._app.at(home.FillForm, **with_user_data).asserts(
            it.IsEqualTo, "Form would be submitted here"
        )
        self._app.at(home.CheckBoxes)
        self._app.at(home.PushButtons, prompt_text="This is a prompt")
        self._app.at(home.InteractWithDynamicElements).asserts(
            it.HasKeyValue, {"hidden_element": "This element was hidden and now is visible!"}
        ).asserts(it.HasKeyValue, {"new_element": "New element added "}).asserts(
            it.HasKeyValue, {"changed_text": "Text changed at"}
        ).asserts(
            it.HasKeyValue,
            {"toggled_class": "This element will change color when class is toggled"},
        # ).asserts(
            # it.HasKeyValue, {"ajax_content": "AJAX content loaded at"}
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
            file_path=f"{CURRENT_DIR}/docs/email.txt",
            multi_file_path=[
                f"{CURRENT_DIR}/docs/email.txt",
                f"{CURRENT_DIR}/docs/UTF8demo.txt",
            ],
        )
        self._app.at(home.InteractWithIFrame).asserts(it.IsEqualTo, "IFrame Content Loaded")
