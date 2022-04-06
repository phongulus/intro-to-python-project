from collections import deque
from model.util import Direction, Point, Color, Pixel


class Snake:
    def __init__(self, width: int, height: int):
        self.screen_width = width
        self.screen_height = height

        self.length: int = 1
        self.color: Color = Color(0, 255, 0)  # Green
        self.direction: Direction = Direction.RIGHT

        mid_point = Point(width // 2, height // 2)
        self.positions: deque[Point] = deque([mid_point])

    def get_head_position(self) -> Point:
        return self.positions[0]

    def turn(self, new_direction: Direction) -> None:
        opposite = Point(new_direction.value.x * -1, new_direction.value.y * -1)

        if self.length == 1 or opposite != self.direction.value:
            self.direction = new_direction

    def move(self, grow: bool = False) -> bool:
        self.length += grow
        curr = self.get_head_position()
        new_x = curr.x + self.direction.value.x
        new_y = curr.y + self.direction.value.y

        if new_x > self.screen_width - 1: 
            new_x = 0

        if new_y > self.screen_height - 1: 
            new_y = 0

        if new_x < 0: 
            new_x = self.screen_width - 1
        
        if new_y < 0: 
            new_y = self.screen_height - 1

        new = Point(new_x, new_y)
        valid_move = new not in self.positions

        self.positions.appendleft(new)

        if not grow:
            self.positions.pop()

        return valid_move

    def reset(self) -> None:
        self.length: int = 1
        self.direction: Direction = Direction.RIGHT

        mid_point = Point(width // 2, height // 2)
        self.positions: deque[Point] = deque([mid_point])

    def draw(self) -> None:
        pass
