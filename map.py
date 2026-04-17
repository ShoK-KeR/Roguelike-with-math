from os import system


class Cell:
    def __init__(self, symbol, can_move):
        self.symbol = symbol
        self.can_move = can_move

    def __repr__(self):
        return self.symbol


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[Cell(".", True) for _ in range(width)] for _ in range(height)]
        self.matrix[0] = [Cell("#", False)] * width
        self.matrix[-1] = [Cell("#", False)] * width
        for i in range(height):
            self.matrix[i][0] = Cell("#", False)
            self.matrix[i][width - 1] = Cell("#", False)

    def is_passable(self, x, y):
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.matrix[y][x].can_move
        return False

    def place_wall(self, x, y):
        self.matrix[y][x] = Cell("#", False)

    def print_map(self, entities):
        buf = [[cell.symbol for cell in row] for row in self.matrix]

        for entity in entities:
            x, y = entity.position
            buf[y][x] = entity.symbol

        system("cls")

        for row in buf:
            print("".join(row))
