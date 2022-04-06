from typing import NamedTuple
from enum import Enum


class Point(NamedTuple):
    x: int
    y: int


class Color(NamedTuple):
    Red: int
    Green: int
    Blue: int


class Direction(Enum):
    UP = Point(0, -1)
    DOWN = Point(0, 1)
    LEFT = Point(-1, 0)
    RIGHT = Point(1, 0)


class Input(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Pixel(object):
    def __init__(self, point, color):
        self.point = point
        self.color = color
