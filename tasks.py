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
        question="Найдите наибольший корень уравнения: x² - 5x + 6 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: x² - 5x + 6\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-2)(x-3)", "(x-3)(x-2)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x² - 7x + 10 = 0", answers=[2]
    ),
    MathTask(
        question="Разложите на множители: x² - 7x + 10\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-2)(x-5)", "(x-5)(x-2)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² + 3x - 18 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: x² + 3x - 18\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+6)(x-3)", "(x-3)(x+6)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x² + 2x - 15 = 0", answers=[-5]
    ),
    MathTask(
        question="Разложите на множители: x² + 2x - 15\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+5)(x-3)", "(x-3)(x+5)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² - 9x + 20 = 0", answers=[5]
    ),
    MathTask(
        question="Разложите на множители: x² - 9x + 20\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-4)(x-5)", "(x-5)(x-4)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x² - 2x - 8 = 0", answers=[-2]
    ),
    MathTask(
        question="Разложите на множители: x² - 2x - 8\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-4)(x+2)", "(x+2)(x-4)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² + x - 12 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: x² + x - 12\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+4)(x-3)", "(x-3)(x+4)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x² - 11x + 28 = 0", answers=[4]
    ),
    MathTask(
        question="Разложите на множители: x² - 11x + 28\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-4)(x-7)", "(x-7)(x-4)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² + 5x - 14 = 0", answers=[2]
    ),
    MathTask(
        question="Разложите на множители: x² + 5x - 14\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+7)(x-2)", "(x-2)(x+7)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² - 8x + 15 = 0", answers=[5]
    ),
    MathTask(
        question="Разложите на множители: x² - 8x + 15\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-3)(x-5)", "(x-5)(x-3)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x² + 6x + 8 = 0", answers=[-4]
    ),
    MathTask(
        question="Разложите на множители: x² + 6x + 8\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+2)(x+4)", "(x+4)(x+2)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² - x - 20 = 0", answers=[5]
    ),
    MathTask(
        question="Разложите на множители: x² - x - 20\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-5)(x+4)", "(x+4)(x-5)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x² + 4x - 21 = 0", answers=[-7]
    ),
    MathTask(
        question="Разложите на множители: x² + 4x - 21\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+7)(x-3)", "(x-3)(x+7)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² - 13x + 36 = 0", answers=[9]
    ),
    MathTask(
        question="Разложите на множители: x² - 13x + 36\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-4)(x-9)", "(x-9)(x-4)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: x² - 3x - 10 = 0", answers=[-2]
    ),
    MathTask(
        question="Разложите на множители: x² - 3x - 10\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-5)(x+2)", "(x+2)(x-5)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² + 8x + 15 = 0", answers=[-3]
    ),
    MathTask(
        question="Разложите на множители: x² + 8x + 15\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x+3)(x+5)", "(x+5)(x+3)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: x² - 6x - 16 = 0", answers=[8]
    ),
    MathTask(
        question="Разложите на множители: x² - 6x - 16\n"
        "  Формат ответа: (x-a)(x-b)  пример: (x-1)(x+2)",
        answers=["(x-8)(x+2)", "(x+2)(x-8)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: 2x² - 10x + 12 = 0", answers=[3]
    ),
    MathTask(
        question="Разложите на множители: 2x² - 10x + 12\n"
        "  Формат ответа: a(x-x1)(x-x2)  пример: 3(x-1)(x+2)",
        answers=["2(x-2)(x-3)", "2(x-3)(x-2)"],
    ),
    MathTask(
        question="Найдите наименьший корень уравнения: 3x² + 9x - 30 = 0", answers=[-5]
    ),
    MathTask(
        question="Разложите на множители: 3x² + 9x - 30\n"
        "  Формат ответа: a(x-x1)(x-x2)  пример: 3(x-1)(x+2)",
        answers=["3(x-2)(x+5)", "3(x+5)(x-2)"],
    ),
    MathTask(
        question="Найдите наибольший корень уравнения: 5x² - 15x - 20 = 0", answers=[4]
    ),
    MathTask(
        question="Разложите на множители: 5x² - 15x - 20\n"
        "  Формат ответа: a(x-x1)(x-x2)  пример: 3(x-1)(x+2)",
        answers=["5(x-4)(x+1)", "5(x+1)(x-4)"],
    ),
]
TASK_POOL_3 = [
    MathTask(
        question="Найдите производную: f(x) = x³", answers=["3x^2"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 3x² dx\n"
        "  Формат ответа: без +C  пример: 2x^5",
        answers=["x^3"],
    ),
    MathTask(
        question="Найдите производную: f(x) = x⁵", answers=["5x^4"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 5x⁴ dx\n"
        "  Формат ответа: без +C  пример: 2x^3",
        answers=["x^5"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 4x³", answers=["12x^2"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 12x² dx\n"
        "  Формат ответа: без +C  пример: 2x^5",
        answers=["4x^3"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 7x²", answers=["14x"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 14x dx\n"
        "  Формат ответа: без +C  пример: 3x^2",
        answers=["7x^2"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 3x⁴", answers=["12x^3"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 12x³ dx\n"
        "  Формат ответа: без +C  пример: 2x^5",
        answers=["3x^4"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 6x", answers=[6]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 6 dx\n"
        "  Формат ответа: без +C  пример: 3x",
        answers=["6x"],
    ),
    MathTask(
        question="Найдите производную: f(x) = x² + 3x", answers=["2x+3", "2x + 3"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ (2x + 3) dx\n"
        "  Формат ответа: без +C  пример: 2x^2+5x",
        answers=["x^2+3x", "x^2 + 3x"],
    ),
    MathTask(
        question="Найдите производную: f(x) = x² - 4x + 1", answers=["2x-4", "2x - 4"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ (2x - 4) dx\n"
        "  Формат ответа: без +C  пример: 2x^2-3x",
        answers=["x^2-4x", "x^2 - 4x"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 5x² + 2x", answers=["10x+2", "10x + 2"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ (10x + 2) dx\n"
        "  Формат ответа: без +C  пример: 3x^2+7x",
        answers=["5x^2+2x", "5x^2 + 2x"],
    ),
    MathTask(
        question="Найдите производную: f(x) = sin(x)", answers=["cos(x)"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ cos(x) dx\n"
        "  Формат ответа: без +C  пример: cos(x)",
        answers=["sin(x)"],
    ),
    MathTask(
        question="Найдите производную: f(x) = cos(x)", answers=["-sin(x)"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ (-sin(x)) dx\n"
        "  Формат ответа: без +C  пример: sin(x)",
        answers=["cos(x)"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 3sin(x)", answers=["3cos(x)"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 3cos(x) dx\n"
        "  Формат ответа: без +C  пример: 5sin(x)",
        answers=["3sin(x)"],
    ),
    MathTask(
        question="Найдите производную: f(x) = -2cos(x)", answers=["2sin(x)"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 2sin(x) dx\n"
        "  Формат ответа: без +C  пример: -5cos(x)",
        answers=["-2cos(x)"],
    ),
    MathTask(
        question="Найдите производную: f(x) = eˣ", answers=["e^x"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ eˣ dx\n"
        "  Формат ответа: без +C  пример: 3e^x",
        answers=["e^x"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 5eˣ", answers=["5e^x"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 5eˣ dx\n"
        "  Формат ответа: без +C  пример: 3e^x",
        answers=["5e^x"],
    ),
    MathTask(
        question="Найдите производную: f(x) = ln(x)", answers=["1/x"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ (1/x) dx\n"
        "  Формат ответа: без +C  пример: 3ln(x)",
        answers=["ln(x)"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 4ln(x)", answers=["4/x"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ (4/x) dx\n"
        "  Формат ответа: без +C  пример: 2ln(x)",
        answers=["4ln(x)"],
    ),
    MathTask(
        question="Найдите производную: f(x) = √x\n"
        "  Формат ответа: пример: 1/(3sqrt(x))",
        answers=["1/(2sqrt(x))"],
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ 1/(2√x) dx\n"
        "  Формат ответа: без +C  пример: 2sqrt(x)",
        answers=["sqrt(x)"],
    ),
    MathTask(
        question="Найдите производную: f(x) = 2x³ - x²", answers=["6x^2-2x", "6x^2 - 2x"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ (6x² - 2x) dx\n"
        "  Формат ответа: без +C  пример: 3x^3-2x^2",
        answers=["2x^3-x^2", "2x^3 - x^2"],
    ),
    MathTask(
        question="Найдите производную: f(x) = x⁴/4", answers=["x^3"]
    ),
    MathTask(
        question="Найдите неопределённый интеграл: ∫ x³ dx\n"
        "  Формат ответа: без +C  пример: x^3/3",
        answers=["x^4/4"],
    ),
]