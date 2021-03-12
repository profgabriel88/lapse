import cv2
import numpy as np
import os

img_a = []

# nome do arquivo gerado
arquivo = 'teste'

modo = int(input("para vídeo digite 0, para gif digite 1, para ambos digite 2: "))

for filename in sorted(os.listdir(os.getcwd())):
	if '.jpg' in filename:
		#print(filename)
		img = cv2.imread(filename)
		height, width, layers = img.shape
		size = (width,height)
		img_a.append(img)

if modo == 0 or modo == 2:
	out = cv2.VideoWriter(f'{arquivo}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, size)

	print('criando mp4')
	for i in range(len(img_a)):
		out.write(img_a[i])
	out.release()

	print('mp4 pronto')
	print('criando avi')

	out = cv2.VideoWriter(f'{arquivo}.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, size)

	for i in range(len(img_a)):
		out.write(img_a[i])
	out.release()
	print('avi pronto')

if modo == 2 or modo == 1:
	# converte as imagens em gif
	print('criando gif')
	os.system(f'convert -delay 10 -loop 0 frame*.jpg {arquivo}.gif')
	print('gif pronto')
