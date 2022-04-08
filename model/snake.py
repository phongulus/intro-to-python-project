from collections import deque
from model.util import Direction, Point, Color


class Snake:
    def __init__(self, width: int, height: int):
        """
        Initializes the snake object and sets its attributes
        of screen_height and screen width

        Parameters:
        ----
        width<int>: width of grid.
        height<int>: height of grid.

        Attributes:
        ----
        screen_width<int>: width of grid
        screen_height<int>:  height of grid
        length<int>: length of snake
        color<Color>: color of the snake
        direction<Direction>: current direction the snake is moving
        positions<deque[Point]>: deque of points the snake is occupying

        """
        self.screen_width = width
        self.screen_height = height

        self.length: int = 1
        self.color: Color = Color(0, 255, 0)  # Green
        self.direction: Direction = Direction.RIGHT

        mid_point = Point(width // 2, height // 2)
        self.positions: deque[Point] = deque([mid_point])

    def get_head_position(self) -> Point:
        """
        Returns the position of the snake's head

        Parameters:
        ----
        None

        Return:
        ----
        <Point>: Point object representing the snake head's current position

        """

        return self.positions[0]

    def turn(self, new_direction: Direction) -> None:
        """
        Sets the snake's direction to the new direction as long
        as the new direction isn't in the exact opposite direction
        to it's current direction.

        Parameters:
        ----
        new_direction<Direction>: the direction the snake is supposed to turn

        Return:
        ----
        None

        """

        opposite = new_direction * Point(-1, -1)

        if self.length == 1 or opposite != self.direction.value:
            self.direction = new_direction

    def move(self, grow: bool = False) -> bool:
        """
        Moves the snake one grid unit in the direction it is facing. Will also
        make the snake grow if the grow param is set to True.
        It will also return a boolean value that expresses if the move was
        valid.

        Parameters:
        ----
        grow<bool>: if the snake is to grow on this move

        Return:
        ----
        <bool>: If the new position of the snake's head is valid.
        Only currently invalid if the snake's head collides with
        the rest of the snake's body.

        """

        self.length += grow
        curr = self.get_head_position()
        new = curr + self.direction.value

        if new.x > self.screen_width - 1:
            new = Point(0, new.y)
        elif new.y > self.screen_height - 1:
            new = Point(new.x, 0)
        elif new.x < 0:
            new = Point(self.screen_width - 1, new.y)
        elif new.y < 0:
            new = Point(new.x, self.screen_height - 1)

        valid_move = new not in self.positions

        self.positions.appendleft(new)

        if not grow:
            self.positions.pop()

        return valid_move

    def reset(self) -> None:
        """
        Resets the snake's length, direction, and positions
        attributes to default values

        Parameters:
        ----
        None

        Return:
        ----
        None

        """

        self.length = 1
        self.direction = Direction.RIGHT

        mid_point = Point(self.screen_width // 2, self.screen_height // 2)
        self.positions = deque([mid_point])
