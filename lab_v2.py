"""Creamos una clase nodo para el manejo de arboles"""
class Nodo():
    def __init__(self,valor,posicion,hijos=[]):
        self.valor=valor
        self.posicion = posicion
        self.hijos=hijos

    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        
    def setPosicion(self,posicion):
        self.posicion=posicion

    def setHijos(self,hijos):
        self.hijos=hijos

def cargarArchivo():
    return[list(linea)[:-1] for linea in open ("Laberinto.txt").readlines()]

def buscar(arbol,posicion):
    if arbol==None:
        return False
    if arbol.posicion==posicion:
        return True
    return buscarhijos(arbol.hijos,posicion) 


def buscarhijos(hijos,posicion):
    if hijos==[]:
        return False
    return buscar(hijos[0],posicion) or buscarhijos(hijos[1:],posicion)


"""Buscamos la posicion x,y en la que se encuentra la 'x'"""
def buscarX(laberinto):
   for x in laberinto:
       for y in range(len(x)):
           if x[y] == "x":
               colocarArbol(laberinto.index(x),y,laberinto) 

raiz=Nodo(0,0,[])
arbol=Nodo(0,0,[])
def colocarArbol(x,y,laberinto):
        raiz.setPosicion((x,y))
        arbol.setPosicion((x,y))
        raiz.setHijos([verIzquierda(x,y,arbol,laberinto),verAbajo(x,y,arbol,laberinto),verArriba(x,y,arbol,laberinto),verDerecha(x,y,arbol,laberinto)])

   
"""Se evaluan los movimentos hacia la derecha, izquierda, abajo y arriba mediante el uso de arboles"""
def verDerecha(x,y,nodo,laberinto):
    print((x,y),"der:")
    if(y+1<=len(laberinto[x])-1 and laberinto[x][y+1]!="1"):
        if(buscar(nodo,(x,y+1))!=True):
            nodo.agregarHijo(Nodo(laberinto[x][y+1],(x,y+1),[]))
            return Nodo(laberinto[x][y+1],(x,y+1),[verAbajo(x,y+1,nodo,laberinto),verArriba(x,y+1,nodo,laberinto),verIzquierda(x,y+1,nodo,laberinto),verDerecha(x,y+1,nodo,laberinto)])
        else:
            return None
    else:
        return None
 
def verIzquierda(x,y,nodo,laberinto):
    print((x,y),"izq:")
    if(y-1>=0 and laberinto[x][y-1]!="1"):
        if(buscar(nodo,(x,y-1))!=True):
            nodo.agregarHijo(Nodo(laberinto[x][y-1],(x,y-1),[]))
            return Nodo(laberinto[x][y-1],(x,y-1),[verAbajo(x,y-1,nodo,laberinto),verArriba(x,y-1,nodo,laberinto),verIzquierda(x,y-1,nodo,laberinto),verDerecha(x,y-1,nodo,laberinto)])
        else:
            return None
    else:
        return None
 
def verAbajo(x,y,nodo,laberinto):
    print((x,y),"abj:")
    if(x+1<=len(laberinto)-1 and laberinto[x+1][y]!="1"):
        if(buscar(nodo,(x+1,y))!=True):
            nodo.agregarHijo(Nodo(laberinto[x+1][y],(x+1,y),[]))
            return Nodo(laberinto[x+1][y],(x+1,y),[verAbajo(x+1,y,nodo,laberinto),verArriba(x+1,y,nodo,laberinto),verIzquierda(x+1,y,nodo,laberinto),verDerecha(x+1,y,nodo,laberinto)])
        else:
            return None
    else:
        return None
 
def verArriba(x,y,nodo,laberinto):
    print((x,y),"arr:")
    if(x-1>=0 and laberinto[x-1][y]!="1"):
        if(buscar(nodo,(x-1,y))!=True):
            nodo.agregarHijo(Nodo(laberinto[x-1][y],(x-1,y),[]))
            return Nodo(laberinto[x-1][y],(x-1,y),[verAbajo(x-1,y,nodo,laberinto),verArriba(x-1,y,nodo,laberinto),verAbajo(x-1,y,nodo,laberinto),verDerecha(x-1,y,nodo,laberinto)])
        else:
            return None
    else:
        return None

def buscarValor(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    return buscarhijosValor(arbol.hijos,valor) 


def buscarhijosValor(hijos,valor):
    if hijos==[]:
        return False
    return buscarValor(hijos[0],valor) or buscarhijosValor(hijos[1:],valor)    

buscarX(cargarArchivo())

if(buscarValor(raiz,"y")==True):
    print("Si tiene solución")
else:
    print("No tiene solución")
