from Tkinter import *

import Image, ImageTk



tk = Tk()

image = Image.open("pic.jpg")

d = image.size

im = ImageTk.PhotoImage(image)



lbl = Label(tk, image=im).grid(row=0, column=1)

#c = Canvas(tk, height=d[0], width=d[1])

#itemid = c.create_image(d[0]/2, d[1]/2, image=im)

#print itemid

#c.grid(row=0, column=1)



pixeles = image.load()

for i in range (0, d[0]):

  for j in range (0, d[1]):

		np = min(pixeles[i, j])

		pixeles[i,j] = (np, np, np)

image.save("gris.jpg")

im2 = ImageTk.PhotoImage(image)



image2  = Image.open("pic.jpg")

pixeles2 = image2.load()

for i in range (0, d[0]):

	for j in range (0, d[1]):

		pp = sum(pixeles[i,j])/3
		if(pp <= 125):

			pixeles2[i,j] = (0, 0, 0)

		else:

			pixeles2[i,j] = (255, 255, 255)

image2.save("negros.jpg")

im3 = ImageTk.PhotoImage(image2)

	

def iniciar():

	lbl = Label(tk, image=im).grid(row=0, column=1)

	print "Reiniciando......"



def grises():  

	lbl = Label(tk, image = im2).grid(row=0, column=1)

	print "Grises......."	



def negros():

	lbl = Label(tk, image = im3).grid(row=0, column=1)

	print "Blanco y Negro...."



bgris = Button(tk, text="Grises", command = grises).grid(row=2, column=0)

bblack = Button(tk, text="Black&White", command = negros).grid(row=2, column=1)

binicio = Button(tk, text="Reset", command = iniciar).grid(row=2, column=2)



tk.mainloop()
