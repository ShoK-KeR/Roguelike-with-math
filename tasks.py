from time import time
import threading


class MathTask:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def check(self, user_input):
        for correct in self.answers:
            if isinstance(correct, int):
                try:
                    if int(user_input) == correct:
                        return True
                except (ValueError, AttributeError):
                    pass
            else:
                normalized = user_input.replace(" ", "").lower()
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
        print("=" * 46)
        print("  ЗАДАНИЕ — реши чтобы атаковать!")
        print("=" * 46)
        print()
        print(self.question)
        print()
        print("  [10 сек]  правильно → КРИТ  (x2 урон)")
        print("  [60 сек]  правильно → УДАР  (x1 урон)")
        print("  [время/мимо]        → МИМО  (x0.5 урон)")
        print()
        print("  Ответ: ", end="", flush=True)

        start = time()
        answer = self._timed_input(timeout=60)
        elapsed = time() - start

        if answer is None or not self.check(answer):
            return "miss"
        elif elapsed <= 10:
            return "crit"
        else:
            return "hit"


TASK_POOL_1 = [
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - 5x + 6 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 5x + 6\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-2)(x-3)", "(x-3)(x-2)"],
    ),
]


TASK_POOL_2 = [
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - 5x + 6 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 5x + 6\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-2)(x-3)", "(x-3)(x-2)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x^2 - 7x + 10 = 0", answers=[2]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 7x + 10\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-2)(x-5)", "(x-5)(x-2)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 + 3x - 18 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: x^2 + 3x - 18\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+6)(x-3)", "(x-3)(x+6)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x^2 + 2x - 15 = 0", answers=[-5]
    ),
    MathTask(
        question="Разложите на множители: x^2 + 2x - 15\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+5)(x-3)", "(x-3)(x+5)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - 9x + 20 = 0", answers=[5]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 9x + 20\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-4)(x-5)", "(x-5)(x-4)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x^2 - 2x - 8 = 0", answers=[-2]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 2x - 8\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-4)(x+2)", "(x+2)(x-4)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 + x - 12 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: x^2 + x - 12\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+4)(x-3)", "(x-3)(x+4)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x^2 - 11x + 28 = 0", answers=[4]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 11x + 28\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-4)(x-7)", "(x-7)(x-4)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 + 5x - 14 = 0", answers=[2]
    ),
    MathTask(
        question="Разложите на множители: x^2 + 5x - 14\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+7)(x-2)", "(x-2)(x+7)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - 8x + 15 = 0", answers=[5]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 8x + 15\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-3)(x-5)", "(x-5)(x-3)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x^2 + 6x + 8 = 0", answers=[-4]
    ),
    MathTask(
        question="Разложите на множители: x^2 + 6x + 8\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+2)(x+4)", "(x+4)(x+2)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - x - 20 = 0", answers=[5]
    ),
    MathTask(
        question="Разложите на множители: x^2 - x - 20\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-5)(x+4)", "(x+4)(x-5)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x^2 + 4x - 21 = 0", answers=[-7]
    ),
    MathTask(
        question="Разложите на множители: x^2 + 4x - 21\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+7)(x-3)", "(x-3)(x+7)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - 13x + 36 = 0", answers=[9]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 13x + 36\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-4)(x-9)", "(x-9)(x-4)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x^2 - 3x - 10 = 0", answers=[-2]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 3x - 10\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-5)(x+2)", "(x+2)(x-5)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 + 8x + 15 = 0", answers=[-3]
    ),
    MathTask(
        question="Разложите на множители: x^2 + 8x + 15\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+3)(x+5)", "(x+5)(x+3)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - 6x - 16 = 0", answers=[8]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 6x - 16\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-8)(x+2)", "(x+2)(x-8)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: 2x^2 - 10x + 12 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: 2x^2 - 10x + 12\n"
        "  Формат ответа: a(x-x1)(x-x2)  пример: 3(x-1)(x+2)",
        answers=["2(x-2)(x-3)", "2(x-3)(x-2)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: 3x^2 + 9x - 30 = 0", answers=[-5]
    ),
    MathTask(
        question="Разложите на множители: 3x^2 + 9x - 30\n"
        "  Формат ответа: a(x-x1)(x-x2)  пример: 3(x-1)(x+2)",
        answers=["3(x-2)(x+5)", "3(x+5)(x-2)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: 5x^2 - 15x - 20 = 0", answers=[4]
    ),
    MathTask(
        question="Разложите на множители: 5x^2 - 15x - 20\n"
        "  Формат ответа: a(x-x1)(x-x2)  пример: 3(x-1)(x+2)",
        answers=["5(x-4)(x+1)", "5(x+1)(x-4)"],
    ),
]

TASK_POOL_3 = [
    MathTask(
        question="Найдите наибольший корень уравнения: x^2 - 5x + 6 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: x^2 - 5x + 6\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-2)(x-3)", "(x-3)(x-2)"],
    ),
]