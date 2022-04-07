from collections import deque
from xmlrpc.client import Boolean
from model.util import Point, Color
import random


class Food:
    def __init__(self, width: int, height: int):
        """
        Initializes the Food object and sets its attributes
        of color and position and points

        Parameters:
        ----
        width<int>: width of grid.
        height<int>: height of grid.

        Attributes:
        ----
        color<Color>: RGB color value of food (Red).
        position<Point>: Position of food.
        all_points<set(Point)>: Set of all points in the grid.
        """

        self.color: Color = Color(255, 0, 0)  # Red
        self.position: Point = Point(1, 1)

        # Get the set of all possible food placement positions.
        # This is useful for move_random_position later.
        self.all_points: set(Point) = set()
        for x in range(width):
            for y in range(height):
                self.all_points.add(Point(x, y))

    def move_random_position(self, snake_pos: deque[Point]) -> Boolean:
        """
        Moves the food to a random position that is not its old position
        and not in the snake.

        Parameters:
        ----
        snake_pos<deque>: snake points

        Return:
        ----
        <Boolean>: Returns True if there are points left and False if not
        """

        set_snake_pos = set(snake_pos)

        difference = self.all_points - set_snake_pos - self.position
        self.position = random.choice(list(difference))

        return len(difference) != 0

    def reset(self):
        """
        Reset the food position to its default position.

        Parameters:
        ----
        None

        Return:
        ----
        None
        """

        self.position = Point(1, 1)
