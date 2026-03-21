from os import system
import random
from msvcrt import getch



def get_key():
    key = getch()
    if key in (b'\xe0', b'\x00'):
        key = getch()
        return {b'H': 'UP', b'P': 'DOWN', b'M': 'RIGHT', b'K': 'LEFT'}.get(key, '')
    return key.decode('utf-8', errors='ignore')


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
        self.matrix = [
            [Cell('.', True) for _ in range(width)]
            for _ in range(height)
        ]
        self.matrix[0]  = [Cell('#', False)] * width
        self.matrix[-1] = [Cell('#', False)] * width
        for i in range(height):
            self.matrix[i][0]       = Cell('#', False)
            self.matrix[i][width-1] = Cell('#', False)

    def is_passable(self, x, y):
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.matrix[y][x].can_move
        return False

    def print_map(self, entities):
        buf = [[cell.symbol for cell in row] for row in self.matrix]

        for entity in entities:
            x, y = entity.position
            buf[y][x] = entity.symbol

        system('cls')

        for row in buf:
            print(''.join(row))


class Person:
    def __init__(self, symbol, health_points, attack_damage,
                 position=(1, 1)):
        self.symbol        = symbol
        self.health_points = health_points
        self.max_hp        = health_points
        self.attack_damage = attack_damage
        self.position      = position

    def __repr__(self):
        return self.symbol

    def is_alive(self):
        return self.health_points > 0

    def move(self, direction, game_map):
        x, y = self.position
        delta = {'UP': (0, -1), 'DOWN': (0, 1),
                 'RIGHT': (1, 0), 'LEFT': (-1, 0)}
        dx, dy = delta.get(direction, (0, 0))
        nx, ny = x + dx, y + dy

        if game_map.is_passable(nx, ny):
            self.prev_position = self.position
            self.position = (nx, ny)

    def take_damage(self, damage):
        self.health_points -= damage
        return damage

    def attack(self, target):
        return target.take_damage(self.attack_damage)
