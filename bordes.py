from time import *

import Image

import math



def convolucion():

	t0 = time()

	imagen = Image.open("gris_borrosa.jpg")  #parte de una imagen gris y con filtro

	pixeles = imagen.load()

	d = imagen.size

	

	#kernelx = ([-1,0,1],

	#	       [-1,0,1],

	#	       [-1,0,1]) #operador x prewitt



	#kernely = ([1,1,1],

	#	       [0,0,0],

	#	       [-1,-1,-1]) #operador y prewitt



	kernelx = ([-1,0,1],

			 [-2,0,2],

			 [-1,0,1]) #operador x sobel



	kernely = ([1,2,1],

			  [0,0,0],

			  [-1,-2,-1]) #operador y sobel



	for i in range (0, d[0]): 

		for j in range (0, d[1]): 

			gx, gy = 0, 0

			

			for x in range (0, 3):

				for y in range (0, 3):



					if(j<=d[0]-3 and i<d[1]-3):					

						conx = kernelx[x][y] * pixeles[i+x, j+y][0]

                                        	cony = kernely[x][y] * pixeles[i+x, j+y][0]

					else:

						conx = 0

						cony = 0	

	

					gx = conx + gx

					gy = cony + gy

					

			g = math.sqrt(math.pow(gx,2)+math.pow(gy,2)) #raiz de gradiente x a la 2 + gradiante y a la 2

			g2 = int(g)

			

			if g2 <= 0:

				g2 = 0

				

			elif g2 >= 255:

				g2 = 255



			pixeles[i,j] = (g2, g2, g2)

			

	

	imagen.save("convol.jpg")

	t1 = time()

	tf = t1 - t0

	print "Tiempo que tardo el procesamiento = "+str(tf)+" segundos"



convolucion()

			
