from behave import (
    given,
    when,
    then,
)  # pylint: disable=no-name-in-module


@given("we have behave installed")
def is_behave_installed(context):
    pass


@when("we implement a test")
def implement(context):
    assert True is not False


@then("behave will test it for us!")
def test_it(context):
    assert context.failed is False
