from Tkinter import *

import Image, ImageTk



tk = Tk()

image = Image.open("pic.jpg")

#pixor = image.load()

image.save("actual.jpg")

im = ImageTk.PhotoImage(image)

im2 =  ImageTk.PhotoImage(image)

actual = Image.open("actual.jpg")

d = actual.size

pixeles = actual.load()



t=0



lbi = Label(tk, image=im).grid(row=2, column=1)

lbc = Label(tk, text=str(t)).grid(row=2, column=2)





def reset():

	global t, pixeles, pixor

	t=0

	image.save("actual.jpg")

	#pixeles = pixor	

	lbi = Label(tk, image=im).grid(row=2, column=1)

	lbc = Label(tk, text=str(t)).grid(row=2, column=2)



def borroso():

	global t, pixeles, actual, lbi, lbc, im2, d

	actual = Image.open("actual.jpg")

	pixeles = actual.load()

	t += 1

	for i in range (0, d[0]):

		for j in range (0, d[1]):

			pixeles[i,j] = promedio(i,j)#tupla de 3 valores

	actual.save("actual.jpg")

	actual.save("borrosa"+str(t)+".jpg")



	im2 = ImageTk.PhotoImage(actual)

	

	lbi = Label(tk).grid(row=2, column=1)

	lbi = Label(tk, image=im2).grid(row=2, column=1)

	lbc = Label(tk, text=str(t)).grid(row=2, column=2)

		



def promedio(i,j): #y,x

	global pixeles

	if(i==0): 

		if(j==0):#esquina superior izquierda

			pd = pixeles[(i+1), j]

			pr = pixeles[i, (j+1)]



			promr = (pd[0] + pr[0]) / 2 

			promg = (pd[1] + pr[1]) / 2

			promb = (pd[2] + pr[2]) / 2 

			

			return (promr, promg, promb)

			

		elif(j==(d[1]-1)):#esquina superior derecha

			pd = pixeles[(i+1), j]

			pl = pixeles[i, (j-1)]



			promr = (pd[0] + pl[0]) / 2

			promg = (pd[1] + pl[1]) / 2 

			promb = (pd[2] + pl[2]) / 2 

			

			return (promr, promg, promb)

		

		else:#orilla arriba

			pd = pixeles[(i+1), j] #y, x

			pl = pixeles[i, (j-1)]

			pr = pixeles[i, (j+1)]



			promr = (pd[0] + pl[0] + pr[0]) / 3

			promg = (pd[1] + pl[1] + pr[1]) / 3 

			promb = (pd[2] + pl[2] + pr[2]) / 3



			return (promr, promg, promb)

			

	elif(i==(d[0]-1)):

		if(j==0):#esquina inferior izquierda

			pu = pixeles[(i-1), j]

			pr = pixeles[i, (j+1)]

			

			promr = (pu[0] + pr[0]) / 2 

			promg = (pu[1] + pr[1]) / 2 

			promb = (pu[2] + pr[2]) / 2 	



			return (promr, promg, promb)		



		elif(j==(d[1]-1)):#esquina inferior derecha

			pu = pixeles[(i-1), j] #y,x

			pl = pixeles[i, (j-1)]



			promr = (pu[0] + pl[0]) / 2 

			promg = (pu[1] + pl[1]) / 2 

			promb = (pu[2] + pl[2]) / 2



			return (promr, promg, promb)

		

		else:#orilla abajo

			pu = pixeles[(i-1), j] #y,x

			pl = pixeles[i, (j-1)]

			pr = pixeles[i, (j+1)]

			

			promr = (pu[0] + pl[0] + pr[0]) / 3

			promg = (pu[1] + pl[1] + pr[1]) / 3 

			promb = (pu[2] + pl[2] + pr[2]) / 3 



			return (promr, promg, promb)

	

	elif(j==0):#orilla izquierda

		pu = pixeles[(i-1), j]

		pd = pixeles[(i+1), j]

		pr = pixeles[i, (j+1)]



		promr = (pu[0] + pd[0] + pr[0]) / 3

		promg = (pu[1] + pd[1] + pr[1]) / 3 

		promb = (pu[2] + pd[2] + pr[2]) / 3 



		return (promr, promg, promb)



	elif(j==(d[1]-1)):#orilla derecha

		pu = pixeles[(i-1), j] #x,y

		pd = pixeles[(i+1), j]

		pl = pixeles[i, (j-1)]



		promr = (pu[0] + pu[0] + pl[0]) / 3

		promg = (pu[1] + pu[1] + pl[1]) / 3 

		promb = (pu[2] + pu[2] + pl[2]) / 3 	



		return (promr, promg, promb)					

		

	else:

		pu = pixeles[(i-1), j] #y,x

		pd = pixeles[(i+1), j]

		pl = pixeles[i, (j-1)]

		#print i,j

		pr = pixeles[i, (j+1)]



		promr = (pu[0] + pd[0] + pl[0] + pr[0]) / 4 

		promg = (pu[1] + pd[1] + pl[1] + pr[1]) / 4 

		promb = (pu[2] + pd[2] + pl[2] + pr[2]) / 4 

	

		return (promr, promg, promb) #tupla de 3 valores



breset = Button(text="Reset", command=reset).grid(row=1, column=2)

bapply = Button(text="Aplicar", command=borroso).grid(row=3, column=2)



mainloop()
