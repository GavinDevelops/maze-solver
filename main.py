from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)


class Cell:
    def __init__(
        self, top_left_point: Point, bottom_right_point: Point, window: Window
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = top_left_point.x
        self.x2 = bottom_right_point.x
        self.y1 = top_left_point.y
        self.y2 = bottom_right_point.y
        self.__win = window

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.__win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.__win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.__win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.__win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        center_one = Point((self.x1 + self.x2) // 2, (self.y1 + self.y2) // 2)
        center_two = Point(
            (to_cell.x1 + to_cell.x2) // 2, (to_cell.y1 + to_cell.y2) // 2
        )
        line = Line(center_one, center_two)
        self.__win.draw_line(line, fill_color)


def main():
    win = Window(800, 600)
    cell1 = Cell(Point(101, 100), Point(200, 200), win)
    cell2 = Cell(Point(201, 200), Point(400, 400), win)
    cell1.draw()
    cell2.draw()
    cell2.draw_move(cell1)
    win.wait_for_close()


if __name__ == "__main__":
    main()
