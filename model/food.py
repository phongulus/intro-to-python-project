from collections import deque
from model.util import Point, Color
import random


class Food:
    def __init__(self, width: int, height: int):
        """
        Initializes the Food object and sets its attributes
        of color and position and points

        Parameters:
        ----
        width<int>: width of grid
        height<int>: height of grid

        Attributes:
        ----
        color<Color>: RGB value of food (Red)
        position<Point>: Position of food
        all_points<list(Point)>: List of points of all points in the grid
        """
        self.color: Color = Color(255, 0, 0)  # Red
        self.position: Point = Point(1, 1)  # TODO: Randomize this

        self.all_points: list(Point) = []
        for x in range(width):
            for y in range(height):
                self.all_points.append(Point(x, y))

    def move_random_position(self, snake_pos: deque[Point]) -> None:
        """
        Moves the food to a random position that is not it's old position
        and not in the snake

        Paramters:
        ----
        snake_pos<deque>: snake points
        """
        # Todo: food cannot appear within the snake body
        self.position = random.choice(self.all_points)

    def draw(self):
        pass
