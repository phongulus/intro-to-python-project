from model.snake import Snake
from model.food import Food
from model.util import Color


class Game:

    def __init__(self, width: int, height: int):
        """
        Initializes the Game object and sets its attributes
        width and height. Also creates a Snake object and a
        Food object.

        Parameters:
        ----
        width<int>: width of grid.
        height<int>: height of grid.

        Attributes:
        ----
        width<int: width of grid.
        height<int>: height of grid.
        snake<Snake>: Snake object to keep track of snake length and position.
        food<Food>: Food object to keep track of food position.
        """

        self.snake = Snake(width, height)
        self.food = Food(width, height)
        self.width = width
        self.height = height

    def update_game(self, last_event) -> None:
        """
        Update the game state (Snake and Food) based on player input
        (or lack thereof).

        Parameters:
        ----
        last_event<Any>: type None, when there are no inputs events to
        process. Type Direction, when there is player input.

        Return:
        ----
        None; game state is modified in-place.
        """

        if last_event:
            self.snake.turn(last_event)

        grow = self.snake.get_head_position() == self.food.position

        if grow:
            self.food.move_random_position(snake_pos=self.snake.positions)

        if not self.snake.move(grow=grow):
            self.snake.reset()
            self.food.reset()

    def get_matrix(self) -> list[list[tuple[int, int, int]]]:
        """
        Get the current game state as a matrix for display on the LED matrix.

        Parameters:
        ----
        None

        Return:
        ----
        mat<list[list[tuple[int, int, int]]]>: The height * width matrix
        where each element is a tuple representing the color of a pixel via
        RGB code in a tuple `(r, g, b)`.
        """

        # Make a blank width * height matrix.
        mat = []
        for _ in range(self.height):
            mat.append([Color(0, 0, 0) for _ in range(self.width)])

        # Update matrix with Food and Snake positions.
        mat[self.food.position.y][self.food.position.x] = self.food.color
        for curr in self.snake.positions:
            mat[curr.y][curr.x] = self.snake.color

        return mat
