from unittest import TestCase
from collections import deque
from model.util import Point, Color
from model.food import Food


class FoodTestCase(TestCase):

    def test_food_init(self):
        """
        Create a new Food object and check the default values.
        """

        f = Food(width=2, height=2)
        assert type(f) == Food
        assert type(f.color) == Color
        assert type(f.position) == Point
        assert type(f.all_points) == set
        assert f.color == Color(255, 0, 0)
        assert f.position == Point(1, 1)
        assert len(
            f.all_points -
            set([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])) == 0

    def test_food_move(self):
        """
        Create a Food object and test its ability to move to a random
        position on the grid.
        """

        f = Food(width=2, height=2)
        assert f.position == Point(1, 1)

        # Check that the food will never stay in the same position.
        old_pos = f.position
        for _ in range(100):
            assert f.move_random_position(deque([]))
            assert f.position != old_pos
            old_pos = f.position

        # Check that the food will never be moved to inside the snake.
        f.position = Point(0, 0)
        assert f.move_random_position(
            deque([Point(0, 0), Point(0, 1), Point(1, 0)])
        )
        assert f.position == Point(1, 1)
        for _ in range(100):
            assert f.move_random_position(
                deque([Point(0, 0), Point(1, 1)])
            )
            assert f.position == Point(0, 1) or f.position == Point(1, 0)

        # Check when there is nowhere to move the food.
        assert not f.move_random_position(
            deque([Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)])
        )
        f.position = Point(1, 1)
        assert not f.move_random_position(
            deque([Point(0, 0), Point(0, 1), Point(1, 0)])
        )

    def test_food_reset(self):
        """
        Check that the reset function correctly sets the food
        to the default position again.
        """

        f = Food(width=2, height=2)
        f.position = Point(0, 0)
        assert f.position != Point(1, 1)
        f.reset()
        assert f.position == Point(1, 1)
