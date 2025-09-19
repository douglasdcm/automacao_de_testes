import pytest
from wrappers.selenium_wrapper import SeleniumWrapper


def time_deleteme(sleep):
    import time

    time.sleep(sleep)


@pytest.fixture
def amazon():
    driver = SeleniumWrapper()
    driver.goto("http://www.amazon.com.br")
    driver.maximaize_window()
    try:
        driver.click_by_xpath("//button")
    except Exception:
        pass
    yield driver
    driver.quit()


class Search:
    def __init__(self, driver: SeleniumWrapper):
        self._driver = driver

    def execute(self):
        self._driver.send_text("twotabsearchtextbox", "brinquedo")
        self._driver.click("nav-search-submit-button")


class FilterProduct:

    def __init__(self, driver: SeleniumWrapper):
        self._driver = driver

    def execute(self):
        FILTER_1 = '//*[@id="p_123/1319472"]//i'
        FILTER_2 = '//*[@id="p_123/683551"]//i'
        self._driver.click_action_xpath(FILTER_1)
        self._driver.click_action_xpath(FILTER_2)


class SelectSecondProduct:

    def __init__(self, driver: SeleniumWrapper):
        self._driver = driver

    def execute(self):
        SECOND_PRODUCT = "//*[@data-component-type='s-search-results']//div[@role='listitem' and @data-index='4']"
        expected_product = self._driver.get_text_by_xpath(SECOND_PRODUCT)
        self._driver.click_by_xpath(SECOND_PRODUCT)
        return expected_product


class AddToCart:

    def __init__(self, driver: SeleniumWrapper):
        self._driver = driver

    def execute(self):
        ADD_TO_CART = "add-to-cart-button"
        self._driver.click(ADD_TO_CART)
        CONFIRMATION = '//*[@id="NATC_SMART_WAGON_CONF_MSG_SUCCESS"]/h1'
        actual_confirmation = self._driver.get_text_by_xpath(CONFIRMATION)
        assert actual_confirmation == "Adicionado ao carrinho"


class InspectCart:

    def __init__(self, driver: SeleniumWrapper):
        self._driver = driver

    def execute(self):
        CART = "nav-cart-count-container"
        self._driver.click(CART)
        MY_PRODUCT = "//h4"
        actual_product = amazon.get_text_by_xpath(MY_PRODUCT)
        # assert actual_product in expected_product


def test_buy_a_product(amazon: SeleniumWrapper):
    Search(amazon).execute()
    FilterProduct(amazon).execute()
    SelectSecondProduct(amazon).execute()
    AddToCart(amazon).execute()
    InspectCart(amazon).execute()
