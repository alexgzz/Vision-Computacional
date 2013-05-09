import Image, ImageDraw

from sys import argv



def filtrom(image):
  pixeles = image.load()
	d = image.size
	for i in range(d[0]):
		for j in range(d[1]):
			puntos = []
			for x in range(-1,2):
				for y in range(-1,2):
					try:
						puntos.append(pixeles[i+x,j+y][0])
					except:
						puntos.append(0)

			puntos.sort()
			h = len(puntos)/2
			if len(puntos) % 2 == 0:
				m = (puntos[h - 1])
			else:
				m = puntos[h]
	
			pixeles[i,j] = (m,m,m)
			
	img2 = "filtrom_"+img
	image.save(img2)
	return img2

def diferencia(image, image2):
	pixeles1 = image.load()
	pixeles2 = image2.load()
	d = image.size
		
	esquinas = []
	for i in range(d[0]):
		for j in range(d[1]):
			dif = (pixeles1[i,j][0]) - (pixeles2[i,j][0])
							
			if dif >20:	
				
				pixeles2[i,j] = (255, 255, 255)
				esquinas.append((i,j))
				
			else:
				pixeles2[i,j] = (0,0,0)

	image2.save("esq_"+img)	
	return esquinas

img = argv[1]
def main():
	image = Image.open(img)

	img2 = filtrom(image)
	image2 = Image.open(img2)
	
	esquinas = diferencia(image, image2)

	draw = ImageDraw.Draw(image2)
	
	esquinas.sort()
	for p in range(len(esquinas)):
		try:
			draw.line((esquinas[p], esquinas[p+1]), fill="rgb(255, 0, 0)")
		except:
			draw.line((esquinas[-1], esquinas[0]), fill="rgb(255, 0, 0)")
			

	image2.save("fin_"+img)
	
main()

	
