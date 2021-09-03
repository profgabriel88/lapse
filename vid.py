import cv2
import numpy as np
import os
from os import system

a = 0

arquivo = input('digite o nome do arquivo de saída: ')
system(f'mkdir {arquivo}')

while(True):
	try:
		img_a = []
		# ordena os arquivos e anexa ao vetor de imagens
		for filename in sorted(os.listdir(f'{a}')):
			if '.jpg' in filename:
				print(filename)
				img = cv2.imread(f'{a}/{filename}')
				# print(img)
				height, width, layers = img.shape
				size = (width,height)
				img_a.append(img)
		
		# cria o arquivo mp4 com base no vetor
		out = cv2.VideoWriter(f'{arquivo}/{arquivo}_{a}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, size)

		print(f'criando mp4 {a}')
		for i in range(len(img_a)):
			out.write(img_a[i])
		out.release()

		print('mp4 pronto')
		
		a += 1
		print(a)
		
	except FileNotFoundError as e:
		break

		
