from collections import deque
from model.util import Direction, Point, Color, Pixel


class Snake:
    def __init__(self, width: int, height: int):
        self.length: int = 1
        self.color: Color = Color(0, 255, 0)  # Green
        self.direction: Direction = Direction.RIGHT

        mid_point = Point(width // 2, height // 2)
        # mid_point = Point(4, 4)
        self.positions: deque[Point] = deque([mid_point])

    def get_head_position(self) -> Point:
        return self.positions[0]

    def turn(self, new_direction: Direction) -> None:
        opposite = Point(new_direction.value.x * -1, new_direction.value.y * -1)

        if self.length == 1 or opposite != self.direction.value:
            print(f"valid turn, cond1: {self.length ==1}, cond2: {opposite != self.direction}")
            self.direction = new_direction

    def move(self, grow: bool = False) -> None:
        self.length += grow
        curr = self.get_head_position()
        new_x = curr.x + self.direction.value.x
        new_y = curr.y + self.direction.value.y

        self.positions.appendleft(Point(new_x, new_y))

        if not grow:
            self.positions.pop()

    def draw(self) -> None:
        pass
