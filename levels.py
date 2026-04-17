from entities import Enemy
from tasks import TASK_POOL_1, TASK_POOL_2, TASK_POOL_3


class Level:
    def __init__(self, map_size, walls, enemies, task_pool, intro_text):
        self.map_size = map_size
        self.walls = walls
        self.enemies = enemies
        self.task_pool = task_pool
        self.intro_text = intro_text


LEVELS = [
    Level(
        map_size=(30, 12),
        walls=(
            [(x, 4) for x in range(2, 13)]
            + [(x, 4) for x in range(15, 28)]
            + [(x, 7) for x in range(4, 16)]
            + [(x, 7) for x in range(18, 28)]
        ),
        enemies=[
            Enemy("g", "Гоблин", position=(5, 2)),
            Enemy("g", "Гоблин", position=(24, 2)),
            Enemy("g", "Гоблин", position=(14, 9)),
        ],
        task_pool=TASK_POOL_1,
        intro_text="Уровень 1. Пойми и почувствуй",
    ),
    Level(
        map_size=(50, 12),
        walls=(
            [(x, 4) for x in range(2, 11)]
            + [(x, 4) for x in range(13, 24)]
            + [(x, 4) for x in range(26, 37)]
            + [(x, 4) for x in range(39, 48)]
            + [(x, 7) for x in range(6, 17)]
            + [(x, 7) for x in range(19, 30)]
            + [(x, 7) for x in range(32, 43)]
            + [(12, y) for y in range(4, 8)]
            + [(25, y) for y in range(4, 8)]
            + [(38, y) for y in range(4, 8)]
        ),
        enemies=[
            Enemy("g", "Гоблин", position=(4, 2)),
            Enemy("g", "Гоблин", position=(20, 2)),
            Enemy("g", "Гоблин", position=(6, 9)),
            Enemy("g", "Гоблин", position=(33, 9)),
            Enemy("O", "Орк", position=(13, 5), health_points=10, attack_damage=4),
            Enemy("O", "Орк", position=(39, 5), health_points=10, attack_damage=4),
        ],
        task_pool=TASK_POOL_2,
        intro_text="Уровень 2. Войди во вкус",
    ),
    Level(
        map_size=(80, 12),
        walls=(
            [(x, 4) for x in range(2, 13)]
            + [(x, 4) for x in range(15, 28)]
            + [(x, 4) for x in range(30, 43)]
            + [(x, 4) for x in range(45, 58)]
            + [(x, 4) for x in range(60, 66)]
            + [(x, 7) for x in range(7, 18)]
            + [(x, 7) for x in range(20, 33)]
            + [(x, 7) for x in range(35, 48)]
            + [(x, 7) for x in range(50, 61)]
            + [(x, 7) for x in range(63, 66)]
            + [(14, y) for y in range(4, 8)]
            + [(29, y) for y in range(4, 8)]
            + [(44, y) for y in range(4, 8)]
            + [(59, y) for y in range(4, 8)]
            + [(67, y) for y in range(1, 5)]
            + [(67, y) for y in range(7, 11)]
            + [(x, 3) for x in range(68, 78)]
            + [(x, 8) for x in range(68, 78)]
        ),
        enemies=[
            Enemy("g", "Гоблин", position=(4, 2)),
            Enemy("g", "Гоблин", position=(20, 2)),
            Enemy("g", "Гоблин", position=(36, 2)),
            Enemy("g", "Гоблин", position=(8, 9)),
            Enemy("g", "Гоблин", position=(24, 9)),
            Enemy("g", "Гоблин", position=(52, 9)),
            Enemy("O", "Орк", position=(15, 5), health_points=10, attack_damage=4),
            Enemy("O", "Орк", position=(45, 5), health_points=10, attack_damage=4),
            Enemy("O", "Орк", position=(64, 5), health_points=10, attack_damage=4),
            Enemy("B", "Босс", position=(75, 6), health_points=30, attack_damage=6),
        ],
        task_pool=TASK_POOL_3,
        intro_text="Уровень 3. РАУ 5.0",
    ),
]
