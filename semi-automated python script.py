
import time
import pyautogui as pg

print("program will run in 10 secs")
time.sleep(10)

for i in range(100):
    pg.write("This is a semi-automated python code.")
    time.sleep(5)
    pg.press("Enter")
