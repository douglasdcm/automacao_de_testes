from selenium import webdriver
from guara.transaction import Application, AbstractTransaction
from guara import it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from wrapper import WrapperSelenium
from transactions import (
    InteractWithDropdowns,
    InteractWithFiles,
    InteractWithIFrames,
    InteractWithTables,
    InteractWithTooltips,
    InteractWtihDynamics,
    NavigateToPage,
    SubtimForm,
    FillCheckbox,
    PushButtons,
)


def test_sample_web_page_ptp():
    app = Application(WrapperSelenium())
    app.at(NavigateToPage)
    app.when(
        SubtimForm,
        with_name="douglas",
        with_password="abc123",
        with_bio="aaa\\naaa",
        with_country="Australia",
        with_age=54,
        with_birthdate="2025-08-28",
        with_email="foo@email.com",
    ).asserts(it.IsEqualTo, "Form would be submitted here")
    app.when(FillCheckbox)
    app.when(PushButtons).asserts(it.IsEqualTo, "Hello, Douglas!")
    app.when(InteractWtihDynamics).asserts(
        it.IsEqualTo, "This element was hidden and now is visible!"
    )
    app.when(InteractWithDropdowns)
    app.when(InteractWithTables).asserts(it.IsEqualTo, "4")
    app.when(InteractWithTooltips).asserts(it.IsEqualTo, "This is a tooltip")
    app.when(InteractWithFiles)
    app.when(InteractWithIFrames).asserts(it.IsEqualTo, "IFrame Content Loaded")
