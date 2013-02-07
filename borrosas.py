from Tkinter import *
import Image, ImageTk


ventana = Tk()

image = Image.open("pic.jpg")

d = image.size

print d[0],"x",d[1]

pixeles = image.load()


def borrosa():

  for i in range (0, d[0]):

		for j in range (0, d[1]):

			pixeles[i,j] = promedio(i,j)#tupla de 3 valores

	image.save("borrosa.jpg")


def promedio(i,j):

	global pixeles

	if(i==0): 

		if(j==0):#esquina superior izquierda

			pd = pixeles[(i+1), (j+1)]

			pr = pixeles[(i+1), j]

			promr = (pd[0] + pr[0]) / 2 

			promg = (pd[1] + pr[1]) / 2

			promb = (pd[2] + pr[2]) / 2 

		

		elif(j==d[1]):#esquina inferior izquierda

			pu = pixeles[(i-1), (j-1)]

			pr = pixeles[(i+1), j]



			promr = (pu[0] + pr[0]) / 2

			promg = (pu[1] + pr[1]) / 2 

			promb = (pu[2] + pr[2]) / 2 

		

		else:#orilla izquierda

			pu = pixeles[(i), (j-1)] #x,y

			pd = pixeles[(i), (j+1)]

			pr = pixeles[(i+1), j]



			promr = (pu[0] + pd[0] + pr[0]) / 3

			promg = (pu[1] + pd[1] + pr[1]) / 3 

			promb = (pu[2] + pd[2] + pr[2]) / 3

			

	elif(i==d[0]):

		if(j==0):#esquina superior derecha

			pd = pixeles[(i), (j+1)]

			pl = pixeles[(i-1), j]

			

			promr = (pd[0] + pl[0]) / 2 

			promg = (pd[1] + pl[1]) / 2 

			promb = (pd[2] + pl[2]) / 2 			



		elif(j==d[1]):#esquina inferior derecha

			pu = pixeles[(i), (j-1)] #x,y

			pl = pixeles[(i-1), j]



			promr = (pu[0] + pl[0]) / 2 

			promg = (pu[1] + pl[1]) / 2 

			promb = (pu[2] + pl[2]) / 2

		

		else:#orilla derecha

			pu = pixeles[(i), (j-1)] #x,y

			pd = pixeles[(i), (j+1)]

			pl = pixeles[(i-1), j]

			

			promr = (pu[0] + pd[0] + pl[0]) / 3

			promg = (pu[1] + pd[1] + pl[1]) / 3 

			promb = (pu[2] + pd[2] + pl[2]) / 3 

	

	elif(j==0):#orilla arriba

		pd = pixeles[(i), (j+1)]

		pl = pixeles[(i-1), j]

		pr = pixeles[(i+1), j]


		promr = (pd[0] + pl[0] + pr[0]) / 3

		promg = (pd[1] + pl[1] + pr[1]) / 3 

		promb = (pd[2] + pl[2] + pr[2]) / 3 


	elif(j==d[1]):#orilla abajo

		pu = pixeles[(i), (j-1)] #x,y

		pl = pixeles[(i-1), j]

		pr = pixeles[(i+1), j]


		promr = (pu[0] + pl[0] + pr[0]) / 3

		promg = (pu[1] + pl[1] + pr[1]) / 3 

		promb = (pu[2] + pl[2] + pr[2]) / 3 	
		

	else:

		pu = pixeles[(i), (j-1)] #x,y

		pd = pixeles[(i), (j+1)]

		pl = pixeles[(i-1), j]

		pr = pixeles[(i+1), j]


		promr = (pu[0] + pd[0] + pl[0] + pr[0]) / 4 

		promg = (pu[1] + pd[1] + pl[1] + pr[1]) / 4 

		promb = (pu[2] + pd[2] + pl[2] + pr[2]) / 4 

	

	return (promr, promg, promb) #tupla de 3 valores

def main():

	borrosa()

main()		
