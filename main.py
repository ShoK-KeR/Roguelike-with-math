from map import Map
from entities import Player, Enemy
from hud import HUD
from msvcrt import getch
from entities import get_key


class Game:
    def __init__(self):
        self.map = Map(24, 16)
        self.player = Player(position=(1, 1))
        self.enemies = [
            Enemy("g", "Гоблин", position=(10, 5)),
            Enemy("G", "Огр", position=(7, 10)),
        ]
        self.max_enemies = len(self.enemies)
        self.hud = HUD()
        self.combat_log = []

    @property
    def all_entities(self):
        return [self.player] + self.enemies

    def update_enemies(self):
        for enemy in self.enemies:
            if enemy.is_alive():
                enemy.ai_step(self.player, self.map, self.combat_log)
        self.enemies = [e for e in self.enemies if e.is_alive()]

    def run(self):
        while True:
            self.map.print_map(self.all_entities)
            self.hud.render(
                self.player, self.enemies, self.max_enemies, self.combat_log
            )

            if not self.player.is_alive():
                print("  Вы погибли. Игра окончена.")
                break

            if not self.enemies:
                print("  Все враги побеждены! Победа!")
                break

            self.combat_log = []
            key = get_key()
            if not self.player.handle_input(
                key, self.map, self.enemies, self.combat_log
            ):
                break

            self.update_enemies()


if __name__ == "__main__":
    Game().run()
