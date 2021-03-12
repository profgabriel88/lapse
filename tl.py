import urllib.request
import numpy as np
import cv2 as cv
from os import system
from time import sleep

# numeração do arquivo
i = 0

# intervalo em segundo entre as fotos
intervalo = 0.01

# endereço ip para usar o celular como camera - App IP Webcam por Pavel Khlebovich
url = "http://:8080/video"


while True:
	# se for usar o celular colocar entre parenteses url
	# cap = cv.VideoCapture(url)
	# se for usar webcam troque o url por um número, 
	# 0 para a camera do notebook ou 1 para webcam usb
    cap = cv.VideoCapture(0)
    
    ret, frame = cap.read()
    cv.imwrite('frame{0:04d}.jpg'.format(i), frame)
    cv.imshow('frame', frame)
    cap.release()       
    print(f'foto {i} capturada')
    #sleep(0.2)
           
    sleep(intervalo)
    
    i += 1
    
    #apertando q o programa encerra
    if cv.waitKey(1) == ord('q'):
       break

print('done')

cv.destroyAllWindows()
