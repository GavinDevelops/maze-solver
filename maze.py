from cell import Cell
from display import Window
from time import sleep


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x,
        cell_size_y,
        win: Window,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for _ in range(self.num_cols):
            col = []
            for _ in range(self.num_rows):
                cell = Cell(self.__win)
                col.append(cell)
            self.__cells.append(col)

        for x in range(len(self.__cells)):
            for y in range(len(self.__cells[x])):
                self.__draw_cell(x, y)

    def __draw_cell(self, x, y):
        x1 = self.x1 + x * self.cell_size_x
        y1 = self.y1 + y * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[x][y].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        sleep(0.05)
