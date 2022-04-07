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
        new = curr + self.direction.value

        if new.x > self.screen_width - 1: 
            new.x = 0

        if new.y > self.screen_height - 1: 
            new.y = 0

        if new.x < 0: 
            new.x = self.screen_width - 1
        
        if new.y < 0: 
            new.y = self.screen_height - 1

        valid_move = new not in self.positions

        self.positions.appendleft(new)

        if not grow:
            self.positions.pop()

        return valid_move

    def reset(self) -> None:
        self.length = 1
        self.direction = Direction.RIGHT

        mid_point = Point(self.screen_width // 2, self.screen_height // 2)
        self.positions = deque([mid_point])
