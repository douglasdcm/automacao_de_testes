from behave import (
    given,
    when,
    then,
)  # pylint: disable=no-name-in-module
from src.ninja import Ninja, NinjaLevel, Opponent


@given("the ninja has a third level black-belt")
def ninja_level(context):
    ninja = Ninja()
    ninja.level = NinjaLevel.THRID_BLACK_BELT.value
    context.ninja = ninja


@when("attacked by a samurai")
def attacked_by_weaker_opponent(context):
    ninja: Ninja = context.ninja
    battle_result = ninja.take_opponent(Opponent.SAMURAI)
    context.battle_result = battle_result


@then("the ninja should engage the opponent")
def engage(context):
    assert context.battle_result == "engage the opponent!!!"


@when("attacked by Chuck Norris")
def attacked_by_powerfull_opponent(context):
    ninja: Ninja = context.ninja
    battle_result = ninja.take_opponent(Opponent.CHUCK_NORIS)
    context.battle_result = battle_result


@then("the ninja should run for his life")
def step_impl(context):
    assert context.battle_result == "run for life!!!"
