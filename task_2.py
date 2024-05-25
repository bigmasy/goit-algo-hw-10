import random
import scipy.integrate as spi


def is_inside(x, y):
    return y <= x**2

def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині трикутника
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area

# Розміри прямокутника
a = 2  # ширина прямокутника
b = 4  # висота прямокутника

# Кількість експериментів
num_experiments = 1000

def f(x):
    return x**2

x = 0
y = 2
quad_result, error = spi.quad(f, x, y)


# Виконання симуляції
mc_result = monte_carlo_simulation(a, b, num_experiments)

# Висновки та порівняння результатів
print(f"Інтеграл методом Монте-Карло: {mc_result}")
print(f"Інтеграл за допомогою функції quad: {quad_result}")

# Порівняння різниці
difference = abs(mc_result - quad_result)
print(f"Різниця між методами: {difference}")

if difference < 0.01:
    print("Метод Монте-Карло дав точний результат.")
else:
    print("Метод Монте-Карло може потребувати більшої кількості вибірок для підвищення точності.")
