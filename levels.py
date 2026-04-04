from entities import Enemy, Boss
from tasks import TASK_POOL_1, TASK_POOL_2, TASK_POOL_3


class Level:
    def __init__(self, map_size, enemies, task_pool, intro_text):
        self.map_size = map_size
        self.enemies = enemies
        self.task_pool = task_pool
        self.intro_text = intro_text


LEVELS = [
    Level(
        map_size=(20, 16),
        enemies=[Enemy('g', 'Гоблин', position=(10, 5))],
        task_pool=TASK_POOL_1,
        intro_text="Уровень 1. Пойми и почувствуй",
    ),
    Level(
        map_size=(24, 18),
        enemies=[Enemy('g', 'Гоблин', position=(10, 5))],
        task_pool=TASK_POOL_2,
        intro_text="Уровень 2. Войди во вкус",
    ),
    Level(
        map_size=(30, 20),
        enemies=[Enemy('g', 'Гоблин', position=(10, 5))],
        task_pool=TASK_POOL_3,
        intro_text="Уровень 3. РАУ 5.0",
    ),
]
