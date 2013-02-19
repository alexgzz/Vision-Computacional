import Image

import random


def bfs(imagen, rcolor, px, altura, ancho):

    pixeles = imagen.load()

    

    (fila, columna) = px

    original = pixeles[fila, columna]

    cola = [(fila, columna)]

     

    while len(cola) > 0:

        (fila, columna) = cola.pop(0)

        actual = pixeles[fila, columna]

        if actual == original or actual == rcolor:

            for dx in [-1, 0, 1]:

                for dy in [-1, 0, 1]:

                    candidato = (fila + dy, columna + dx)

                    if candidato[0] >= 0 and candidato[0] < altura and candidato[1] >= 0 and candidato[1] < ancho:

                        contenido = pixeles[candidato[0], candidato[1]]

                        if contenido == original:

                            pixeles[candidato[0], candidato[1]] = rcolor

                            cola.append(candidato)

    return imagen 




def main():
    imagen = Image.open("bin_mapa.jpg")
    pixeles = imagen.load()

    d = imagen.size

    colores = []

    cantidades = []

    for x in range(d[0]):

        for y in range(d[1]):

            if pixeles[x, y] == (0, 0, 0):

				rcolor = (random.randint(0,256), random.randint(0,256), random.randint(0, 256))
				imagen2 = bfs(imagen, rcolor, (x, y), d[0], d[1]) 
				colores.append(rcolor)

    #checar el color mas usado            

    for i in range(len(colores)):

	cantidades.insert(i, (colores.count(i)))



    maximo = max(cantidades)

    lugar = cantidades.index(maximo)

    c_fondo = colores[lugar]

    print c_fondo



    for i in range(0,d[0]):

		for j in range(0, d[1]):

			p=pixeles[i, j]

			if(p==c_fondo):

				pixeles[i, j]=(p[0], p[0], p[0])



    imagen2.save("final_mapa.jpg")



main()     
