import cv
import Image, ImageDraw

from sys import argv
import time



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

			

	#img2 = "filtrom_"+img

	#image.save(img2)

	return image



def diferencia(image, image2):#filtrom, gris

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



	#image2.save("esq_"+img)	

	return esquinas

def grises(image):
	pixeles = image.load()

	d = image.size
	#print "dimensiones: ", d
	for i in range (0, d[0]):

		for j in range (0, d[1]):

 

			pp = sum(pixeles[i,j])/3

			pixeles[i,j] = (pp, pp, pp)
						
	return image

def bgr_to_rgb(image):
	pixeles = image.load()
	d = image.size

	for i in range(d[0]):
		for j in range(d[1]):
			(b, g, r) = pixeles[i, j]
			pixeles[i, j] = (r, g, b)
		
	return image

def rgb_to_bgr(image):
	pixeles = image.load()
	d = image.size

	for i in range(d[0]):
		for j in range(d[1]):
			(r, g, b) = pixeles[i, j]
			pixeles[i, j] = (b, g, r)
		
	return image

def pintar(image, text):
	pixeles = image.load()
	d = image.size
	x = (d[0]-420)/2#110
	y = (d[1]-420)/2#30
	draw = ImageDraw.Draw(image)
	
	c = "rgb(0,0,255)"
	a=10	
	if(text==1):
		c = "rgb(0,255,0)" #pinta verde si detecto el mosaico en el recuadro
		for note in info:
			draw.text((x+5,y+a), str(note), fill="rgb(0,200,50)")
			a += 20

	draw.line(((x, y), (x+420, y)), fill=c)
	draw.line(((x+420, y), (x+420, y+420)), fill=c)
	draw.line(((x, y), (x, y+420)), fill=c)
	draw.line(((x, y+420), (x+420, y+420)), fill=c)		
				
	return image

def color_test(image):
	#image = bgr_to_rgb(image)

	d = image.size

	pix = image.load()
	x = (d[0]-420)/2#110
	y = (d[1]-420)/2#30
	x2 = x+420
	y2 = y+420



	rojos = []

	verdes = []

	azules = []

	

	for i in range(x, x2):

		for j in range(y, y2):

			(r, g, b)= pix[i, j]

			rojos.append(r)

			verdes.append(g)

			azules.append(b)

			

	rp = (sum(rojos))/(len(rojos))

	vp = (sum(verdes))/(len(verdes))

	ap = (sum(azules))/(len(azules))



	colorp = (rp, vp, ap)

	#print "color pixel 1 =", pix[0,0]

	#image = rgb_to_bgr(image)#rgb a bgr		


	print "\nColor promedio =", colorp


	#porcentajes de variacion

	varr = ( ( (colorp[0]) - (colorref[0]) )/ 255.0 ) * 100.0 

	varv = ( ( (colorp[1]) - (colorref[1]) )/ 255.0 ) * 100.0

	vara = ( ( (colorp[2]) - (colorref[2]) )/ 255.0 ) * 100.0



	var = (varr, varv, vara)



	notas = []

	for i in range(len(var)):

		if(var[i] == 0):

			notas.append("igual a la referencia y pasa la prueba")

		elif (var[i] < 0):

			if(abs(var[i]) < tolerancia):

				notas.append("por debajo de la referencia y pasa la prueba")

			else:

				notas.append("por debajo de la referencia y no pasa la prueba")

		else:

			if(abs(var[i]) < tolerancia):

				notas.append("por encima de la referencia y pasa la prueba")

			else:

				notas.append("por encima de la referencia y no pasa la prueba")


	result = []

	print "Variaciones del promedio respecto a la referencia:\n"
	result.append("Variaciones del promedio respecto a la referencia:")
	

	print "Azul : ", "%.2f" % var[0], "%", notas[0]
	result.append("Azul: " +str("%.2f" % var[0]) +"%" +" "+ str(notas[0]))
	

	print "Verde : ", "%.2f" % var[1], "%", notas[1]
	result.append("Verde: " +str("%.2f" % var[1]) +"%" +" "+ str(notas[1]))
	

	print "Rojo : ", "%.2f" % var[2], "%", notas[2]
	result.append("Rojo: " +str("%.2f" % var[2]) +"%" +" "+ str(notas[2]))
	

	return result	

def detectar_objeto(image): #checa los valores de los contornos dentro del recuadro
	pixeles = image.load()
	d = image.size

	x = (d[0]-420)/2#110
	y = (d[1]-420)/2#30
	x2 = x+420
	y2 = y+420

	p1 = pixeles[x+1,y+1]
	p2 = pixeles[x2-1, y+1]
	p3 = pixeles[640/2, 480/2]
	p4 = pixeles[x+1, y2-1]
	p5 = pixeles[x2-1, y2-1]

	ps = [p1,p2,p3,p4,p5]
	vs = []

	for i in range(len(ps)):
		v1 = ps[0][0] - ps[i][0]
		v2 = ps[0][1] - ps[i][1]
		v3 = ps[0][2] - ps[i][2]
		vs.append(sum((v1,v2,v3))/3)

	detect = 0
	#if(p1==p2 or p1==p3 or p1==p4 or p1==p5 or p2==p3 or p2==p4 or p2==p5 or p3==p4 or p3==p5 or p4==p5):
	if(sum(vs)/len(vs) <= 10):
		detect = 1
	
	return detect			
	
cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(0)
#actual = Image.new("RGB",(640, 480))
info = []
r = int(argv[1])
g = int(argv[2])
b = int(argv[3])
colorref = [r, g, b]
tolerancia = float(argv[4])

while True:
    img = cv.QueryFrame(capture)
    #cv.SaveImage("BGR.jpg", img)
    #gray = cv.CreateImage((img.width,img.height), 8, 1)
    #cv.CvtColor(img, gray, cv.CV_BGR2GRAY)#escala de grises
    #cv.CvtColor(img, img, cv.CV_BGR2RGB)#bgr a rgb
    p_img = Image.fromstring("RGB", cv.GetSize(img), img.tostring()) #imagen pil
    #gr_img = Image.fromstring("RGB", cv.GetSize(img), img.tostring())
    
    #p_img = bgr_to_rgb(p_img)#convertir de formato bgr a rgb
    #p_img.save("RGB.jpg")
    
    
    #p_img = grises(p_img)#pasar a escala de grises

    #fm_img = filtrom(gr_img)#aplicar filtro mediano

    #esquinas = diferencia(gr_img, fm_img)
       
    #info = ["Rojo 52% debajo de la referecia y no pasa","Verde 13% debajo de la referecia y no pasa","Azul 11% debajo de la referecia y no pasa"]
    p_img = pintar(p_img, 0)

    detect = detectar_objeto(p_img)
    
    if(detect == 1):
    	t1 = time.time()
    	info = color_test(p_img)
    	p_img = pintar(p_img, 1)
    	t2 = time.time()
    #print "Tiempo de procesamiento", t2-t1

    #p_img = rgb_to_bgr(p_img)#rgb a bgr

    cv_img = cv.CreateImageHeader(p_img.size, cv.IPL_DEPTH_8U, 3) #imagen opencv
    cv.SetData(cv_img, p_img.tostring())
    #cv.CvtColor(cv_img, cv_img, cv.CV_RGB2BGR)#rgb a bgr
    #cv.SaveImage("FIN.jpg", cv_img)
    
    cv.ShowImage("camera", cv_img)
    if cv.WaitKey(10) == 27:
        break
