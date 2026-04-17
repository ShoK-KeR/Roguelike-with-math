from map import Map
from entities import Player
from hud import HUD
from entities import get_key
from levels import LEVELS
from os import system


class Game:
    def __init__(self):
        self.current_level_index = 0
        self.player = Player(position=(1, 1))
        self.hud = HUD()
        self.combat_log = []
        self.load_level()

    def load_level(self):
        level = LEVELS[self.current_level_index]
        self.map = Map(*level.map_size)
        for x, y in level.walls:
            self.map.place_wall(x, y)
        self.enemies = level.enemies
        self.max_enemies = len(self.enemies)
        self.task_pool = level.task_pool

    def next_level(self):
        self.current_level_index += 1
        if self.current_level_index >= len(LEVELS):
            return False
        self.player.position = (1, 1)
        self.player.health_points = self.player.max_hp
        self.combat_log = []
        self.load_level()
        return True

    @property
    def all_entities(self):
        return [self.player] + self.enemies

    def update_enemies(self):
        for enemy in self.enemies:
            if enemy.is_alive():
                enemy.ai_step(self.player, self.map, self.combat_log)
        self.enemies = [e for e in self.enemies if e.is_alive()]

    def show_level_intro(self):
        level = LEVELS[self.current_level_index]
        system("cls")
        print("=" * 46)
        print(f"  {level.intro_text}")
        print(f"  Уровень {self.current_level_index + 1} из {len(LEVELS)}")
        print("=" * 46)
        print()
        cmd = input("  Нажмите Enter или введите команду: ").strip()

        if cmd.startswith("goto "):
            try:
                n = int(cmd.split()[1]) - 1
                if 0 <= n < len(LEVELS):
                    self.current_level_index = n
                    self.load_level()
            except (ValueError, IndexError):
                pass

    def run(self):
        self.show_level_intro()

        while True:
            self.map.print_map(self.all_entities)
            self.hud.render(
                self.player,
                self.enemies,
                self.max_enemies,
                self.combat_log,
                self.current_level_index + 1,
            )

            if not self.player.is_alive():
                print("  Вы погибли. Игра окончена.")
                break

            if not self.enemies:
                system("cls")
                print("=" * 46)
                print(f"  Уровень {self.current_level_index + 1} пройден!")
                print("  Поздравляем!")
                print("=" * 46)
                print()
                print("  Нажмите любую клавишу для продолжения...")
                get_key()

                if not self.next_level():
                    system("cls")
                    print("=" * 46)
                    print("  Вы прошли игру! Поздравляем!")
                    print("=" * 46)
                    break

                self.show_level_intro()
                continue

            self.combat_log = []
            key = get_key()
            if not self.player.handle_input(
                key, self.map, self.enemies, self.combat_log, self.task_pool
            ):
                break

            self.update_enemies()


if __name__ == "__main__":
    Game().run()
