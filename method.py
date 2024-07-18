import numpy as np
import cv2
import imutils
from IPython.display import Image, display

# Функция для отображения изображения
def imshow(img, filename):
    cv2.imwrite(filename, img)
    display(Image(filename))

# Чтение изображения
image = cv2.imread("7.png")

# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение гауссовского размытия для уменьшения шума
gray = cv2.GaussianBlur(gray, (9, 9), 0)

# Сохранение промежуточного результата
imshow(gray, "test7.png")

# Применение оператора Кэнни для выделения границ
edge = cv2.Canny(gray, 10, 250)

# Сохранение промежуточного результата
imshow(edge, "edge7.png")

# Создание структурного элемента и применение морфологической операции закрытия
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
closed = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)

# Сохранение промежуточного результата
imshow(closed, "closed7.png")

# Нахождение контуров на изображении
cnt = cv2.findContours(closed.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = imutils.grab_contours(cnt)

# Вывод найденных контуров
print(cnt)

total = 0

# Обработка каждого контура
for c in cnt:
    # Вычисление периметра контура
    p = cv2.arcLength(c, True)
    
    # Аппроксимация контура
    approx = cv2.approxPolyDP(c, 0.02 * p, True)
    print(approx)
    
    # Проверка, является ли контур четырехугольником
    if len(approx) == 4:
        # Отрисовка контура на изображении
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1

# Вывод общего числа найденных четырехугольников
print(total)

# Сохранение итогового изображения
imshow(image, "test_final7.png")
