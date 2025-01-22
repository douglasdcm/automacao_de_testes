from enum import Enum


class NinjaLevel(Enum):
    THRID_BLACK_BELT = 3


class Opponent:
    CHUCK_NORIS = "chuck_norris"
    SAMURAI = "samurai"


class Ninja:
    def __init__(self):
        self.__level = None

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    def take_opponent(self, skill_level: str):
        if self.__level != NinjaLevel.THRID_BLACK_BELT.value:
            return "Ninja level not defined."
        if skill_level == Opponent.SAMURAI:
            return "engage the opponent!!!"
        if skill_level == Opponent.CHUCK_NORIS:
            return "run for life!!!"
        return "invalid skill_level"
