import statistics
"------------------------"

def promedio(lista):

    suma = 0
    cont = len(lista)


    for componente in lista:
        suma += componente


    avarage = suma / cont

    return avarage

"------------------------"

def componente_mayor(lista):

    mayor = lista[0]


    for componente in lista:

        if componente > mayor:
            mayor = componente

    return mayor

"------------------------"

def eliminar_componente_menor(lista):


    menor_componente = lista[0]
    posicion_menor_componente = 0


    componentes_cont = len(lista)


    componente_suma = 0


    posicion_cont = 0

    for componente in lista:


        if componente < menor_componente:

            posicion_menor_componente = posicion_cont
            menor_componente = componente


        posicion_cont += 1


    lista.pop(posicion_menor_componente)


    return lista

def desviacion_estandar(lista):

    d = statistics.stdev(lista)

    return d