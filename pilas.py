class Pila():
    def __init__(self):
        self.datos = []

    def apilar (self, elementos):
        self.datos.append(elementos)

    def vacia(self):
        return len(self.datos) == 0

    def tope(self):
        if self.vacia():
            print("esta vacia")
        else:
            return self.datos[-1]
        
    def desapilar(self):
        if self.vacia():
            print("error")
        else: 
            return self.datos.pop()
        
    

pila = Pila()
pila.apilar(10)    
pila.apilar(15)  
pila.apilar(12)  


print ("pila luego de apilar", pila.datos)
print ("valor que esta en el tope", pila.tope())

dato = pila.desapilar()
print ("pila desapilada", pila.datos)
print ("dato desapilado", dato)

