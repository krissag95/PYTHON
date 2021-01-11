import pyautogui
from pynput import keyboard as kb
import threading

flag = True

def start_click(key):
    global flag
    if key == kb.KeyCode.from_char('+'):
        print("Starting +")
        flag = True
        thread = threading.Thread(target=clicking)
        thread.start()
    elif key == kb.KeyCode.from_char('-'):
        print('Stopping -')
        flag = False
    elif key == kb.KeyCode.from_char('*'):
        print('Finishing *')
        thread.stop()
        quit()

def clicking():
    global flag
    x, y = pyautogui.position()
    print(f"x={x}, y={y}")
    while flag:
        pyautogui.click(x,y,clicks=20,button='left')

with kb.Listener(on_press=start_click) as listener:
    listener.join()
    

    
    
        