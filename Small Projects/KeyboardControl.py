import pyautogui
import time

message = input("Enter the message: ")
for i in range(100):
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(0.5)
