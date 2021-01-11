import cv2
import numpy as np

#Imagen completa para analizar
img_rgb = cv2.imread('screen2.png')
#Imagen que se va a detectar 
template = cv2.imread('Cursor.png')

#Ancho y alto del template
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb,template, cv2.TM_CCOEFF_NORMED)

#Porcentaje de match dentro de la imagen
threshold = .95

loc = np.where(res >= threshold)

#ciclo para ubicar las coincidencias
for pt in zip(*loc[::-1]):
    #cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
    print(f"click=({pt[0]+w/2},{pt[1]+h/2})")
    
#Guardar imagen con las coincidencias marcadas en un rectangulo
cv2.imwrite('result.png',img_rgb)