import pyautogui as autogui
import numpy as np
import time

step = 10
num = 5
array = np.arange(0, step* num, num).reshape(1, -1)
arrayX = np.repeat(array, num, axis = 0)
arrayY = arrayX.T

arrayXList = arrayX.flatten()
arrayYList = arrayY.flatten()

autogui.moveTo(100, 100)

for j in range(len(arrayXList)):
    print(arrayXList[j], arrayYList[j])
    autogui.moveTo(arrayXList[j], arrayYList[j])
    time.sleep(0.1)