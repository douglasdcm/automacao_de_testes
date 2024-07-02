# Referências
# https://screenpy-docs.readthedocs.io/en/latest/example/all_together.html

from screenpy import AnActor, given, then, when
from screenpy.actions import See

import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from screenpy.resolutions import BaseResolution
from hamcrest.core.base_matcher import BaseMatcher


DRIVER = webdriver.Chrome()


# hability
class SubmitFormAbility:
    result = None


class AccessHomePageAbility:
    title = None


# action
class AccessHomePageAction:
    def perform_as(self):
        file_path = pathlib.Path(__file__).parent.resolve()
        DRIVER.get(f"file:///{file_path}/sample.html")
        DRIVER.implicitly_wait(0.5)
        AccessHomePageAbility.title = DRIVER.title


class SubmitFormAction:
    def perform_as(self):
        text = ["cheese", "selenium", "test", "bla", "foo"]
        random_value = text[random.randrange(len(text))]
        text_box = DRIVER.find_element(by=By.ID, value="input")
        text_box.send_keys(random_value)
        submit_button = DRIVER.find_element(by=By.CSS_SELECTOR, value="button")
        submit_button.click()
        SubmitFormAbility.result = DRIVER.find_element(by=By.ID, value="result").text


# question
class TheResultQuestion:
    def answered_by(self, the_actor: AnActor):
        return the_actor.ability_to(SubmitFormAbility).result


class TheTitleQuestion:
    def answered_by(self, the_actor: AnActor):
        return the_actor.ability_to(AccessHomePageAbility).title


# Resolution
def the_matcher(value):
    class IsTextEquals(BaseMatcher):
        def __init__(self, value) -> None:
            super().__init__()
            self.__value = value

        def _matches(self, item):
            return self.__value in item

        def describe_to(self, description):
            """Description used when a negated match fails."""
            description.append_text(f"the result should be {self.__value}")

    return IsTextEquals(value)


class TheResultResolution:
    def resolve(self):
        return the_matcher("It works")


# -----
def the_title_matcher(value):
    class IsTextEquals(BaseMatcher):
        def __init__(self, value) -> None:
            super().__init__()
            self.__value = value

        def _matches(self, item):
            return self.__value == item

        def describe_to(self, description):
            """Description used when a negated match fails."""
            description.append_text(f"the title should be {self.__value}")

    return IsTextEquals(value)


class TheTitleResolution:
    def resolve(self):
        return the_title_matcher("Sample page")


def test_screenplay():
    Neco = AnActor("Neco").who_can(SubmitFormAbility()).who_can(AccessHomePageAbility())
    Neco.perform(AccessHomePageAction)
    given(Neco).was_able_to(AccessHomePageAction)
    then(Neco).should(See.the(TheTitleQuestion(), TheTitleResolution()))

    when(Neco).attempts_to(SubmitFormAction)
    then(Neco).should(See.the(TheResultQuestion(), TheResultResolution()))
