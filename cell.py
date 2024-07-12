from display import Point, Line, Window


class Cell:
    def __init__(self, window: Window | None = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.__win.draw_line(line, "white")
        else:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.__win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.__win.draw_line(line, "white")
        else:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.__win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.__win.draw_line(line, "white")
        else:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.__win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.__win.draw_line(line, "white")
        else:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.__win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        fill_color = "red"
        if undo:
            fill_color = "gray"
        if self.x1 is None or self.x2 is None or self.y1 is None or self.y2 is None:
            return
        center_one = Point((self.x1 + self.x2) // 2, (self.y1 + self.y2) // 2)
        center_two = Point(
            (to_cell.x1 + to_cell.x2) // 2, (to_cell.y1 + to_cell.y2) // 2
        )
        line = Line(center_one, center_two)
        self.__win.draw_line(line, fill_color)
