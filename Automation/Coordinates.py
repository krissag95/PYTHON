import pyautogui
from pynput import keyboard as kb
import threading

def start_click(key):
    global flag
    if key == kb.KeyCode.from_char('+'):
        print("Starting "+str(key))
        x, y = pyautogui.position()
        pyautogui.moveTo(1572,451)
        
        #pyautogui.click(1572,451,clicks=1,button='left')
        print(f"x={x}, y={y}")

    elif key == kb.KeyCode.from_char('-'):
        print('Stopping -')
        flag = False
    elif key == kb.KeyCode.from_char('*'):
        print('Finishing')
        quit()

with kb.Listener(on_press=start_click) as listener:
    listener.join()