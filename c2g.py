import Image, ImageTk

image = Image.open("pic.jpg")

d = image.size

print d[0],"x",d[1]

pixeles = image.load()



for i in range (0, d[0]):

  for j in range (0, d[1]):

		np = min(pixeles[i, j])

		pixeles[i,j] = (np, np, np)

image.save("gris_min.bmp")
