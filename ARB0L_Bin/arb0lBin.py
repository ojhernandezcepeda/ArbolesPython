class ArbolBin:
    def __init__(self, valor,izq=None,der=None):
        self.valor=valor
        self.izquierda=izq
        self.derecha=der

def buscar(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    if valor<arbol.valor:
        return buscar(arbol.izquierda,valor)
    return buscar(arbol.derecha,valor)

def inOrden(arbol):
  if arbol != None:
      inOrden(arbol.izquierda)
      print(arbol.valor)
      inOrden(arbol.derecha)
      
def insertar (arbol,valor):
    if arbol==None:
        return ArbolBin(valor)
    if valor<arbol.valor:
        return ArbolBin(arbol.valor,insertar(arbol.izquierda,valor),arbol.derecha)
    return ArbolBin(arbol.valor,arbol.izquierda,insertar(arbol.derecha,valor))
      
def listarEnArbol(arbol, lista):
    if lista==[]:
        return arbol
    else:
        return listarEnArbol(insertar(arbol,lista[0]),lista[1:])
    
   

inOrden(listarEnArbol((ArbolBin(15,ArbolBin(10,ArbolBin(0)),ArbolBin(55, ArbolBin(25)))),[5,50,20,30,35,45,40]))
