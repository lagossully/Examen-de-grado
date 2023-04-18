#arbol btree estructura de datos

class nodo: #clase nodo
    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor
        self.izq = None
        self.der = None

    def __str__(self):
        return str(self.llave) + " " + str(self.valor)
    
class arbol: #clase arbol
    def __init__(self):
        self.raiz = None

    def insertar(self, llave, valor):
        if self.raiz == None:
            self.raiz = nodo(llave, valor)
        else:
            self.insertar_nodo(self.raiz, llave, valor)

    def insertar_nodo(self, nodo, llave, valor):
        if llave < nodo.llave:
            if nodo.izq == None:
                nodo.izq = nodo(llave, valor)
            else:
                self.insertar_nodo(nodo.izq, llave, valor)
        else:
            if nodo.der == None:
                nodo.der = nodo(llave, valor)
            else:
                self.insertar_nodo(nodo.der, llave, valor)

    def buscar(self, llave):
        if self.raiz == None:
            return None
        else:
            return self.buscar_nodo(self.raiz, llave)

    def buscar_nodo(self, nodo, llave):
        if nodo == None:
            return None
        elif nodo.llave == llave:
            return nodo.valor
        elif llave < nodo.llave:
            return self.buscar_nodo(nodo.izq, llave)
        else:
            return self.buscar_nodo(nodo.der, llave)

    def __str__(self):
        return self.imprimir(self.raiz)

    def imprimir(self, nodo):
        if nodo == None:
            return ""
        else:
            return self.imprimir(nodo.izq) + str(nodo) + self.imprimir(nodo.der)

    def eliminar(self, llave):
        self.raiz = self.eliminar_nodo(self.raiz, llave)

    def eliminar_nodo(self, nodo, llave):
        if nodo == None:
            return None
        elif llave < nodo.llave:
            nodo.izq = self.eliminar_nodo(nodo.izq, llave)
        elif llave > nodo.llave:
            nodo.der = self.eliminar_nodo(nodo.der, llave)
        else:
            if nodo.izq == None and nodo.der == None:
                nodo = None
            elif nodo.izq == None:
                nodo = nodo.der
            elif nodo.der == None:
                nodo = nodo.izq


arbolito = arbol()

if __name__ == "__main__":
    arbolito.insertar(1, "hola")
    arbolito.insertar(2, "mundo")
    arbolito.insertar(3, "cruel")
    arbolito.insertar(4, "de")
    arbolito.insertar(5, "python")
    print(arbolito)
    print(arbolito.buscar(3))
    arbolito.eliminar(3)
    print(arbolito)