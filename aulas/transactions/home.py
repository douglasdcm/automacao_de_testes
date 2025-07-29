# Copyright (C) 2025 Guara - All Rights Reserved
# You may use, distribute and modify this code under the
# terms of the MIT license.
# Visit: https://github.com/douglasdcm/guara

from guara.transaction import AbstractTransaction
from pages.form import Form
from wrappers.base_wrapper import BaseWrapper


class SubmitForm(AbstractTransaction):
    """Transaction to submit a form with a username.
    Args:
        usernarme (str): The username to be submitted in the form.
        password (str): The password to be submitted in the form.
        email (str): The email to be submitted in the form.
        bio (str): The bio to be submitted in the form.
        country (str): The country to be selected in the form.
        age (int): The age to be submitted in the form.
        birthdate (str): The birthdate to be submitted in the form.
    """

    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        self._driver.send_text("username", kwargs.get("username"))
        self._driver.send_text("password", kwargs.get("password"))
        self._driver.send_text("email", kwargs.get("email"))
        self._driver.send_text("bio", kwargs.get("bio"))
        self._driver.select("country", kwargs.get("country"))
        self._driver.send_text("age", kwargs.get("age"))
        self._driver.send_text("birthdate", kwargs.get("birthdate"))
        self._driver.click("submit-btn")
        return self._driver.get_dialog_text()


class FillPreferences(AbstractTransaction):
    def do(self, **kwargs):
        pass


class PushButtons(AbstractTransaction):
    def do(self, **kwargs):
        pass


class InteractWithDynamicElements(AbstractTransaction):
    def do(self, **kwargs):
        pass


class SelectPreferences(AbstractTransaction):
    def do(self, **kwargs):
        pass


class InteractWithTable(AbstractTransaction):
    def do(self, **kwargs):
        pass


class ShowPopover(AbstractTransaction):
    def do(self, **kwargs):
        pass


class UploadFiles(AbstractTransaction):
    def do(self, **kwargs):
        pass


class InteractWithIFrame(AbstractTransaction):
    def do(self, **kwargs):
        pass
