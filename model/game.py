import model.snake as snake_
import model.food as food_
from model.util import Color


class Game:

    def __init__(self, width: int, height: int):
        self.snake = snake_.Snake(width, height)
        self.food = food_.Food(width, height)
        self.width = width
        self.height = height

    def update_game(self, last_event) -> None:

        if last_event:
            self.snake.turn(last_event)

        grow = self.snake.get_head_position() == self.food.position

        if grow:
            self.food.move_random_position(snake_pos=self.snake.positions)

        if not self.snake.move(grow=grow):
            self.snake.reset()
            self.food.reset()

    def get_matrix(self) -> list[list[tuple[int, int, int]]]:
        
        # Make a blank width * height matrix.
        mat = []
        for _ in range(self.height):
            mat.append([Color(0, 0, 0) for _ in range(self.width)])

        # Update matrix with Food and Snake positions.
        mat[self.food.position.y][self.food.position.x] = self.food.color
        for curr in self.snake.positions:
            mat[curr.y][curr.x] = self.snake.color

        return mat