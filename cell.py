from display import Line, Point, Window


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
