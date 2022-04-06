from collections import deque
from model.util import Point, Color
import random


class Food:
    def __init__(self, width: int, height: int):
        self.color: Color = Color(255, 0, 0)  # Red
        self.position: Point = Point(1, 1)  # TODO: Randomize this

        self.all_points: list(Point) = []
        for x in range(width):
            for y in range(height):
                self.all_points.append(Point(x, y))

    def move_random_position(self, snake_pos) -> None:
        # Todo: food cannot appear within the snake body
        self.position = random.choice(self.all_points)

    def reset(self):
        self.position = Point(1, 1)

    def draw(self):
        pass