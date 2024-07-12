from cell import Cell
from display import Window
from time import sleep
import random


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x,
        cell_size_y,
        win: Window | None = None,
        seed=None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.cells = []
        self.seed = seed
        if seed is not None:
            self.seed = random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self._reset_cells_visited()

    def __create_cells(self):
        for _ in range(self.num_cols):
            col = []
            for _ in range(self.num_rows):
                cell = Cell(self.__win)
                col.append(cell)
            self.cells.append(col)

        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                self.__draw_cell(x, y)

    def __draw_cell(self, x, y):
        x1 = self.x1 + x * self.cell_size_x
        y1 = self.y1 + y * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[x][y].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        sleep(0.05)

    def __break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self.__draw_cell(0, 0)
        self.cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            to_visit = []

            if i > 0 and not self.cells[i - 1][j].visited:
                to_visit.append([i - 1, j])
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                to_visit.append([i + 1, j])
            if j > 0 and not self.cells[i][j - 1].visited:
                to_visit.append([i, j - 1])
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                to_visit.append([i, j + 1])

            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return

            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]
            if next_index[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False

    def __solve_r(self, i, j):
        self.__animate()
        self.cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        # left
        if (
            i > 0
            and self.cells[i - 1][j].visited == False
            and self.cells[i][j].has_left_wall == False
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self.__solve_r(i - 1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i - 1][j], undo=True)
        # right
        if (
            i < self.num_cols - 1
            and self.cells[i + 1][j].visited == False
            and self.cells[i][j].has_right_wall == False
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self.__solve_r(i + 1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i + 1][j], undo=True)
        # down
        if (
            j > 0
            and self.cells[i][j - 1].visited == False
            and self.cells[i][j].has_top_wall == False
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self.__solve_r(i, j - 1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j - 1], undo=True)
        # up
        if (
            j < self.num_rows - 1
            and self.cells[i][j + 1].visited == False
            and self.cells[i][j].has_bottom_wall == False
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self.__solve_r(i, j + 1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j + 1], undo=True)
        return False

    def solve(self):
        return self.__solve_r(0, 0)
