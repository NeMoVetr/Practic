import matplotlib.pyplot as plt
import numpy as np

# Функция для генерации данных с вогнутым увеличением с случайными вариациями
def generate_concave_magnification(num_points):
    x = np.linspace(0, 2, num_points)
    # Введение вариабельности в параметры квадратичной функции
    a = np.random.uniform(0.1, 15)
    b = np.random.uniform(1, 10)
    c = np.random.uniform(5, 50)
    y = a * x ** 2 + b * x + c
    t = None
    return x, y, t

# Функция для генерации данных с вогнутым уменьшением с случайными вариациями
def generate_concave_reduction(num_points):
    x = np.linspace(0.1, 5, num_points)
    # Введение вариабельности в параметры квадратичной функции
    a = np.random.uniform(-20, -1)
    b = np.random.uniform(0, 20)
    c = np.random.uniform(1, 14)
    y = (-a / (x + c)) + b
    t = None
    return x, y, t

# Функция для генерации данных с выпуклым увеличением с случайными вариациями
def generate_convex_magnification(num_points):
    x = np.linspace(0.1, 5, num_points)
    # Введение вариабельности в параметры квадратичной функции
    a = np.random.uniform(-100, -0.01)
    b = np.random.uniform(1, 100)
    c = np.random.uniform(1, 50)
    y = (a / (x + c)) + b
    t = None
    return x, y, t

# Функция для генерации данных с выпуклым уменьшением с случайными вариациями
def generate_convex_reduction(num_points):
    x = np.linspace(0, 2, num_points)
    # Введение вариабельности в параметры квадратичной функции
    a = np.random.uniform(0.4, 20)
    b = np.random.uniform(-5, 4)
    c = np.random.uniform(10, 50)
    y = -a * x ** 2 + b * x + c
    t = None
    return x, y, t

# Функция для генерации данных с линейным увеличением с случайными вариациями
def generate_linear_magnification(num_points):
    x = np.linspace(0, 2, num_points)
    # Введение вариабельности в параметры линейной функции
    a = np.random.uniform(0.3, 20)
    b = np.random.uniform(-50, 25)
    y = a * x + b
    t = 1
    return x, y, t

# Функция для генерации данных с линейным уменьшением с случайными вариациями
def generate_linear_reduction(num_points):
    x = np.linspace(0, 2, num_points)
    # Введение вариабельности в параметры линейной функции
    a = np.random.uniform(-10, 0.1)
    b = np.random.uniform(-10, 10)
    y = a * x + b
    t = 2
    return x, y, t

# Функция для генерации данных с резким увеличением
def generate_abrupt_increase(num_points):
    x = np.linspace(0, 2, num_points)
    y = np.zeros_like(x)  # Создаем массив нулей для y

    # Генерируем случайное число скачков (1 или 2)
    num_jumps = np.random.choice([2, 6])

    for _ in range(num_jumps):
        abrupt_index = np.random.randint(10, num_points - 10)  # Случайный индекс, где будет скачок
        y[abrupt_index:] = np.random.uniform(y.max(), y.max() + 10)  # Генерируем случайные значения после скачка

    # Добавляем случайную прямую с произвольным углом наклона
    angle = np.random.uniform(-np.pi / 4, np.pi / 4)  # Случайный угол наклона в радианах
    intercept = np.random.uniform(y.min(), y.max())  # Случайное смещение по оси y
    y += np.tan(angle) * x + intercept
    t = None
    return x, y, t

# Функция для генерации данных с резким уменьшением
def generate_abrupt_decrease(num_points):
    x = np.linspace(0, 2, num_points)
    y = np.zeros_like(x)  # Создаем массив нулей для y

    # Генерируем случайное число скачков (1 или 2)
    num_jumps = np.random.choice([2, 10])

    for _ in range(num_jumps):
        abrupt_index = np.random.randint(10, num_points - 10)  # Случайный индекс, где будет скачок
        y[abrupt_index:] = np.random.uniform(y.min() - 10, y.min())  # Генерируем случайные значения после скачка

    # Добавляем случайную прямую с произвольным углом наклона
    angle = np.random.uniform(-np.pi / 4, np.pi / 4)  # Случайный угол наклона в радианах
    intercept = np.random.uniform(y.min(), y.max())  # Случайное смещение по оси y
    y += np.tan(angle) * x + intercept
    t = None
    return x, y, t

# Функция для создания и сохранения графика
def save_plot(plot_number):
    x, y, t = generate_abrupt_decrease(512)  # Генерация данных с 512 точками

    plt.figure()
    if t is None:
        plt.plot(x, y, linewidth=3, color='black')
    if t == 2:
        plt.ylim(bottom=min(y) - np.random.uniform(0, 50))
        plt.plot(x, y, linewidth=3, color='black')
    elif t == 1:
        plt.ylim(bottom=min(y) + 1, top=max(y) + np.random.uniform(0.1, 10))
        plt.plot(x, y, linewidth=3, color='black')

    plt.title(f'FIG {plot_number}')
    plt.savefig(f'test/abrupt_decrease/plot{i}.png')
    plt.close()

# Генерация и сохранение 1000 графиков
for i in range(1, 1001):
    save_plot(i)
