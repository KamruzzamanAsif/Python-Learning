import pyautogui
import time

for i in range(100):
    pyautogui.write("Magic")
    pyautogui.press('enter')
    time.sleep(0.3)
