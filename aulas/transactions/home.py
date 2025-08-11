# Copyright (C) 2025 Guara - All Rights Reserved
# You may use, distribute and modify this code under the
# terms of the MIT license.
# Visit: https://github.com/douglasdcm/guara

from guara.transaction import AbstractTransaction
from pages.form import Form
from wrappers.base_wrapper import BaseWrapper


class FillForm(AbstractTransaction):
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
        result = self._driver.get_dialog_text()
        self._driver.dismiss_alert()
        return result


class CheckBoxes(AbstractTransaction):

    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        self._driver.click("simple-dropdown")
        self._driver.click("interest-sports")
        self._driver.click("interest-music")
        self._driver.click("gender-female")
        self._driver.click("terms")


class PushButtons(AbstractTransaction):
    """Transaction to interact with various buttons and alerts.
    Args:
        prompt_text (str): The text to be sent to the prompt dialog.
    """

    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        self._driver.click("simple-btn")
        self._driver.dismiss_alert()

        self._driver.click("alert-btn")
        self._driver.dismiss_alert()

        self._driver.click("confirm-btn")
        self._driver.dismiss_alert()
        self._driver.dismiss_alert()

        self._driver.click("prompt-btn")
        self._driver.send_text_to_alert(kwargs.get("prompt_text"))
        self._driver.dismiss_alert()

        self._driver.store_original_tab()
        self._driver.click("new-tab-btn")
        self._driver.close_current_tab()
        self._driver.restore_original_tab()

        self._driver.click("disabled-btn")


class InteractWithDynamicElements(AbstractTransaction):

    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        result = {}
        self._driver.click("show-hidden-btn")
        hidden_element = self._driver.get_text_by_css("#hidden-element")
        result["hidden_element"] = hidden_element

        self._driver.click("add-element-btn")
        new_element = self._driver.get_text_by_css("#element-container > div:nth-child(1)")
        result["new_element"] = new_element

        self._driver.click("change-text-btn")
        changed_text = self._driver.get_text("changeable-text")
        result["changed_text"] = changed_text

        self._driver.click("toggle-class-btn")
        toggled_class = self._driver.get_text("class-toggle-element")
        result["toggled_class"] = toggled_class

        self._driver.click("ajax-btn")
        self._driver.wait_for_text("ajax-content", "AJAX content loaded at")

        ajax_response = self._driver.get_text("ajax-content")
        result["ajax_content"] = ajax_response
        return result


class SelectDropdowns(AbstractTransaction):
    """Transaction to interact with dropdowns and multi-select elements.
    Args:
        simple_option (str): The option to be selected in the simple dropdown.
        multi_options (list): The options to be selected in the multi-select dropdown.
        dynamic_option (str): The option to be selected in the dynamic dropdown.
    """

    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        self._driver.select("simple-dropdown", kwargs.get("simple_option"))

        for option in kwargs.get("multi_options"):
            self._driver.select("multi-select", option)

        self._driver.click("add-option-btn")
        self._driver.click("add-option-btn")
        self._driver.select("dynamic-dropdown", kwargs.get("dynamic_option"))


class InteractWithTable(AbstractTransaction):
    """Transaction to interact with a table, including adding, removing, and sorting rows.

    returns:
        dict: A dictionary containing the results of the interactions with the table.
        - original_number_of_rows (int): The number of rows before any interaction.
        - new_number_of_rows (int): The number of rows after adding a new row.
        - new_row_text (str): The text of the newly added row.
        - number_of_rows_after_delete (int): The number of rows after removing a row.
    """

    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        result = {}
        result["original_number_of_rows"] = self._driver.get_number_of_rows("users-table")
        self._driver.click("add-row-btn")
        result["new_number_of_rows"] = self._driver.get_number_of_rows("users-table")
        result["new_row_text"] = self._driver.get_text_by_css(
            "#users-table > tbody > tr:nth-child(4) > td:nth-child(2)"
        )

        self._driver.click("remove-row-btn")
        result["number_of_rows_after_delete"] = self._driver.get_number_of_rows("users-table")

        return result


class ShowPopover(AbstractTransaction):
    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        return self._driver.hover_over_by_class_name("tooltip")


class UploadFiles(AbstractTransaction):
    """Transaction to upload files.
    Args:
        file_path (str): The path to the file to be uploaded.
        multi_file_path (str): The path to the second file to be uploaded.
    """

    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        self._driver.send_text("file-upload", kwargs.get("file_path"))
        for file in kwargs.get("multi_file_path"):
            self._driver.send_text(
                "multi-file-upload",
                file,
                clear=False,
            )


class InteractWithIFrame(AbstractTransaction):
    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        self._driver.click("load-iframe-btn")
        self._driver.switch_to_frame("sample-iframe")
        return self._driver.get_text_by_css("h3")
