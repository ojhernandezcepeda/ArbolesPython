class ArbolBin():
    def __init__(self, valor, izq = None, der = None):
        self.valor= valor
        self.izquierda = izq
        self.derecha=der
        
def inorden(arbol):
    if arbol==None:
        return ""
    else:
        return inorden(arbol.izquierda)+arbol.valor+inorden(arbol.derecha)
    
def preorden(arbol):
     if arbol==None:
        return ""
     else:
        return arbol.valor+preorden(arbol.izquierda)+preorden(arbol.derecha)
    
def posorden(arbol):
    if arbol==None:
        return ""
    else:
        return posorden(arbol.izquierda)+posorden(arbol.derecha)+arbol.valor
    

arbol = ArbolBin('10 ',ArbolBin('5 '),ArbolBin('20 ',ArbolBin('15 '),ArbolBin('25 ')))
print("pre: "+preorden(arbol))
print("in: "+inorden(arbol))
print("pos: "+posorden(arbol))
