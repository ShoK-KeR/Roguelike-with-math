from os import system
import random
from msvcrt import getch
import threading
import time



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


class MathTask:
    def __init__(self, question, answers):
        self.question  = question
        self.answers    = answers

    def check(self, user_input):
        for correct in self.answers:
            if isinstance(correct, int):
                try:
                    if int(user_input) == correct:
                        return True
                except (ValueError, AttributeError):
                    pass
            else:
                normalized = user_input.replace(' ', '').lower()
                if normalized == correct:
                    return True
        return False

    def _timed_input(self, timeout):
        result = [None]

        def ask():
            try:
                result[0] = input()
            except Exception:
                pass

        t = threading.Thread(target=ask)
        t.daemon = True
        t.start()
        t.join(timeout)
        return result[0]

    def run(self):
        print('=' * 46)
        print('  ЗАДАНИЕ — реши чтобы атаковать!')
        print('=' * 46)
        print()
        print(self.question)
        print()
        print('  [10 сек]  правильно → КРИТ  (x2 урон)')
        print('  [60 сек]  правильно → УДАР  (x1 урон)')
        print('  [время/мимо]        → МИМО  (x0.5 урон)')
        print()
        print('  Ответ: ', end='', flush=True)

        start   = time.time()
        answer  = self._timed_input(timeout=60)
        elapsed = time.time() - start

        if answer is None or not self._check(answer):
            return 'miss'
        elif elapsed <= 10:
            return 'crit'
        else:
            return 'hit'
        

TASK_POOL = [
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - 5x + 6 = 0",
        answers=[3]
    ),

    MathTask(
        question="Разложите на множители: x^2 - 5x + 6\n"
                 "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-2)(x-3)", "(x-3)(x-2)"]  # оба порядка скобок засчитываются
    ),
]

