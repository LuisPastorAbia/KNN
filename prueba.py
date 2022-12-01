from array import *
from operator import attrgetter
import math

#clase distancia/color
class DistanceColor(object):
    """ Distancia a un punto de un punto de color color 
    :param distancia: distancia
    :type distancia: double
    :param color: color of the point
    :type color: str
    """
    def __init__(self,distancia,color):
        self.distancia=distancia
        self.color=color
    def __repr__(self):
        return str(str(self.distancia)+' '+self.color)

#clase Punto
class Point(object):
    """ Punto de color
    :param x: x coordenate
    :type x: double
    :param y: y coordenate
    :type y: double
    :param color: color of the point
    :type color: str
    """
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    def __repr__(self):
        return str(self.x)
    def distancia(self,xcoord,ycoord):
        return DistanceColor(math.sqrt((self.x-xcoord)**2+(self.y-ycoord)**2),self.color)

#Conjunto de datos del ejercicio
myArray=[Point(1,7,'g'),
       Point(1,12,'g'),
       Point(1.5,9,'r'),
       Point(2,5,'g'),
       Point(2,9,'g'),
       Point(2,11,'g'),
       Point(3,2,'r'),
       Point(3,6,'g'),
       Point(3,10,'g'),
       Point(3.5,8,'g'),
       Point(3.75,3,'r'),
       Point(4,2,'r'),
       Point(5.1,3,'r'),
       Point(5.6,4,'r'),
       Point(6.1,1,'r'),
       Point(7,2,'r')]

kParameter= int(input("Introduce un numero entero: "))
xPuntoCentral=float(input("Introduce coordenada X del punto a estudiar "))
yPuntoCentral=float(input("Introduce coordenada Y del punto a estudiar "))

#calculo las distancias y color)
myDistance=map(lambda e: e.distancia(xPuntoCentral,yPuntoCentral), myArray)

#creo la lista del iterable
lista=list(myDistance)

#ordeno el array por la distancia
lista=sorted(lista,key=attrgetter('distancia'))

#borro los más lejanos que el kParameter
del lista[kParameter:]

#cuento g y v para ver quien gana
rojos= sum(1 for i in lista if i.color=='r')
verdes=sum(1 for i in lista if i.color=='g')

if rojos>verdes: print('rojo')
if verdes>rojos: print('verde')
if verdes==rojos: print('empate')

#busqueda de kParameter para el punto dado que sea empate (repito lo anterior pero cambiando el k en el rango posible hasta encontrar el empate)

for i in range(1,17):
    #inicializo los contadores
    rojos=0
    verdes=0
    #vuelvo a crear el iterable para contener todos
    myDistance=map(lambda e: e.distancia(xPuntoCentral,yPuntoCentral), myArray)

    #creo la lista del iterable
    lista=list(myDistance)

    #ordeno el array por la distancia
    lista=sorted(lista,key=attrgetter('distancia'))

    #borro los más lejanos que el kParameter
    del lista[i:]

    #cuento g y v para ver quien gana
    rojos= sum(1 for j in lista if j.color=='r')
    verdes=sum(1 for j in lista if j.color=='g')

    #auxiliar para ir viendo como itera: 
    #print(str(i)+" "+str(rojos)+" "+str(verdes))

    if verdes==rojos: 
        print('empate en el K'+str(i))
        break
    #para parar de calcular una vez encuentre el valor de K

