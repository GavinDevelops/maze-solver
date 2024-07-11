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


def main():
    win = Window(800, 600)
    line1 = Line(Point(0, 2), Point(3, 8))
    line2 = Line(Point(5, 3), Point(9, 10))
    line3 = Line(Point(2, 0), Point(50, 80))
    line4 = Line(Point(0, 2), Point(300, 299))
    win.draw_line(line1, "red")
    win.draw_line(line2, "black")
    win.draw_line(line3, "red")
    win.draw_line(line4, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
