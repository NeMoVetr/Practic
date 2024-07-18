import random
import time

import PyDesmos as PD
import pyautogui


# генерация графика
def desmos(a):
    with PD.Graph('my graph') as G:
        f, y = G.f, G.y
        G(f'y={a}', color='#000000', lineWidth=3.5)


image = pyautogui.screenshot()
for i in range(10):
    # задание параметра
    desmos(random.randint(-100, 100))
    time.sleep(6)
    # создание скриншота
    image1 = pyautogui.screenshot(f"C:\\...\\image{i}.png", region=(122, 77, 1280 - 177, 1024 - 175))
