from collections import deque

#LIFO - Pilas
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)
pila.pop()
print(pila)
n = pila.pop()
print(pila)
print(n)
""" Pop solo puede usarse cuando la pila tiene elementos, si no tiene tira error"""

#FIFO - Colas
cola = deque(["Juan", "Pablo", "Miguel"])
cola.append("Maria")
cola.append("Jose")
print(cola)
cola.popleft()
#popleft() solo funciona en una cola no puede usarse en una lista comun o en una pila
print(cola)
n = cola.popleft()
print(cola)
print(n)
