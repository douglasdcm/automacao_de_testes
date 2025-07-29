# Copyright (C) 2025 Guara - All Rights Reserved
# You may use, distribute and modify this code under the
# terms of the MIT license.
# Visit: https://github.com/douglasdcm/guara

from pytest import mark
from transactions import home, setup
from guara.transaction import Application
from guara import it


class TestTransactionsV1:
    def setup_method(self, method):
        self._app = Application()
        self._app.at(
            setup.OpenApp,
        )

    def teardown_method(self, method):
        self._app.at(setup.CloseApp)

    @mark.skip(reason="This test is skipped for now")
    def test_aulas(self):
        self._app.at(home.SubmitForm).asserts(it.IsEqualTo, None)
