import cv2
import numpy as np
import pyautogui
from time import sleep

#Imagen completa para analizar
screenshot = pyautogui.screenshot()
screenshot.save("Screenshot.png")
sleep(.5)
img_rgb = cv2.imread('Screenshot.png')
#Imagen que se va a detectar 
template = cv2.imread('Cursor.png')

#Ancho y alto del template
w, h = template.shape[:-1]
cw, ch = int(template.shape[:-1]/2)

res = cv2.matchTemplate(img_rgb,template, cv2.TM_CCOEFF_NORMED)

#Porcentaje de match dentro de la imagen
threshold = .95

loc = np.where(res >= threshold)
location = list(zip(*loc[::-1]))
#ciclo para ubicar las coincidencias

for pt in location:
    #cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
    print(f"click=({pt[0]+cw},{pt[1]+ch})")
    print(pt)
    
#Guardar imagen con las coincidencias marcadas en un rectangulo
cv2.imwrite('result.png',img_rgb)