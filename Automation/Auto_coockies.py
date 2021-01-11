import cv2
import numpy as np
import pyautogui
from pynput import keyboard as kb
from time import sleep
import threading

flag = True
pause = False

def obj_detect(img_template):
    global flag
    global pause
    while flag:
        #Imagen completa para analizar (Screenshot)
        screenshot = pyautogui.screenshot()
        screenshot.save("Screenshot.png")
        sleep(.5)
        img_rgb = cv2.imread('Screenshot.png')
        #Imagen que se va a detectar 
        template = img_template
        #Ancho y alto del template
        w, h = template.shape[:-1]
        #Punto medio para hacer click
        cw, ch = int(w/2), int(h/2)

        res = cv2.matchTemplate(img_rgb,template, cv2.TM_CCOEFF_NORMED)
        #Porcentaje de match dentro de la imagen
        threshold = .9

        loc = np.where(res >= threshold)
        #ciclo para ubicar las coincidencias
        pt = list(zip(*loc[::-1]))
        if (len(pt)>0):
            #for pt in location:
            #cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
            #cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
            print(f"click=({pt[0][0]+cw},{pt[0][1]+ch})")
            pause = True
            sleep(.1)
            pyautogui.click(pt[0][0]+cw,pt[0][1]+ch,clicks=1,button='left')
        
            
        #Guardar imagen con las coincidencias marcadas en un rectangulo
        #cv2.imwrite('result.png',img_rgb)
        sleep(2)

def clicking():
    global flag
    global pause
    x, y = pyautogui.position()
    print(f"x={x}, y={y}")
    while flag:
        #print(f"x={x}, y={y}")
        if pause:
            sleep(.2)
            pause =  False
        else:
            pyautogui.click(x,y,clicks=30,button='left')

def start_click(key):
    global flag
    template = cv2.imread('GCCenter.png')
    if key == kb.KeyCode.from_char('+'):
        print("Starting "+str(key))
        flag = True
        hand_detect = threading.Thread(target=obj_detect, args=(template,))
        autoclick = threading.Thread(target=clicking)
        autoclick.start()
        hand_detect.start()
    elif key == kb.KeyCode.from_char('-'):
        print("Stopping "+str(key))
        flag = False
    elif key == kb.KeyCode.from_char('*'):
        print("Finishing"+str(key))
        quit()


with kb.Listener(on_press=start_click) as listener:
    listener.join()