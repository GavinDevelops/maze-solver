from cell import Cell
from display import Point, Window


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
