'''
Tira fotos em intervalos constantes para elaboração de time lapse
Gabriel Dai
'''

import numpy as np
import cv2 as cv
from os import system
from time import sleep
import sys

i = 0
p = 0

# cria pasta para armazenar as fotos
system(f'mkdir {p}')

# intervalo em segundo entre as fotos
intervalo = 0.01

# linkpara usar o celular como webcam através de aplicativo.
url = "http://:8080/video"


while True:
    try:
	
        cap = cv.VideoCapture(url)
        ret, frame = cap.read()
        cv.imwrite(f'{p}/frame{i:04d}.jpg', frame)
        
	# para exibir a imagem capturada remova o comentário da linha a seguir
	#cv.imshow('frame', frame)
	
        cap.release()  
	
	# contador de imagens
        print(f'foto {i} capturada')
        
        sleep(0.2)
            
        sleep(intervalo)
        
        i += 1
        
	# a cada 500 fotos uma nova pasta é criada
        if i == 499:
            i = 0
            p += 1
            system(f'mkdir {p}')

    # caso a conexão com o celular seja interrompida ou perdida
    # o programa imprime o erro e tenta executar novamente até
    # restabelecer a conexão
    except Exception as e:
        # e = sys.exc_info()[0]
        if e.code == -215:
            print( "<p>Error: %s</p>" % e )

print('done')

cv.destroyAllWindows()
