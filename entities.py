import random
from msvcrt import getch


def get_key():
    key = getch()
    if key in (b"\xe0", b"\x00"):
        key = getch()
        return {b"H": "UP", b"P": "DOWN", b"M": "RIGHT", b"K": "LEFT"}.get(key, "")
    return key.decode("utf-8", errors="ignore")


class Person:
    def __init__(self, symbol, health_points, attack_damage, position=(1, 1)):
        self.symbol = symbol
        self.health_points = health_points
        self.max_hp = health_points
        self.attack_damage = attack_damage
        self.position = position

    def __repr__(self):
        return self.symbol

    def is_alive(self):
        return self.health_points > 0

    def move(self, direction, game_map):
        x, y = self.position
        delta = {"UP": (0, -1), "DOWN": (0, 1), "RIGHT": (1, 0), "LEFT": (-1, 0)}
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


class Player(Person):
    KEY_MAP = {
        "UP": "UP",
        "w": "UP",
        "DOWN": "DOWN",
        "s": "DOWN",
        "RIGHT": "RIGHT",
        "d": "RIGHT",
        "LEFT": "LEFT",
        "a": "LEFT",
    }

    def __init__(self, position=(1, 1)):
        super().__init__("@", health_points=20, attack_damage=6, position=position)

    def attack(self, target, log, task_pool):
        task = random.choice(task_pool)
        result = task.run()

        if result == "crit":
            damage = self.attack_damage * 2
            log.append(f"[КРИТ] А ты хорош! Урон: {damage}")
        elif result == "hit":
            damage = self.attack_damage
            log.append(f"[УДАР] Молодец, но есть куда стараться. Урон: {damage}")
        else:
            damage = self.attack_damage // 2
            log.append(f"[МИМО] Нужно больше тренироваться. Урон: {damage}")

        target.take_damage(damage)

    def handle_input(self, key, game_map, enemies, log, task_pool):
        if key == "q":
            return False

        direction = self.KEY_MAP.get(key)
        if not direction:
            return True

        dx, dy = {"UP": (0, -1), "DOWN": (0, 1), "RIGHT": (1, 0), "LEFT": (-1, 0)}[
            direction
        ]
        tx, ty = self.position[0] + dx, self.position[1] + dy

        target = next((e for e in enemies if e.position == (tx, ty)), None)
        if target:
            self.attack(target, log, task_pool)
        else:
            self.move(direction, game_map)

        return True


class Enemy(Person):
    def __init__(
        self, symbol="e", name="Враг", position=(5, 5), health_points=8, attack_damage=3
    ):
        super().__init__(
            symbol,
            health_points=health_points,
            attack_damage=attack_damage,
            position=position,
        )
        self.name = name

    def ai_step(self, player, game_map, log):
        px, py = player.position
        ex, ey = self.position

        if abs(px - ex) + abs(py - ey) == 1:
            dmg = self.attack(player)
            log.append(f"[{self.symbol}] {self.name} атакует вас: -{dmg} HP")
            return

        if abs(px - ex) > abs(py - ey):
            direction = "RIGHT" if px > ex else "LEFT"
        else:
            direction = "DOWN" if py > ey else "UP"

        self.move(direction, game_map)
