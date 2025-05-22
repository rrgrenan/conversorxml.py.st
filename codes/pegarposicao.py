import time
import pyautogui as pa

pa.hotkey('alt', 'tab')
pa.press('tab',2)

time.sleep(5)
print(pa.position())

time.sleep(5)
print(pa.position())