from queue import PriorityQueue
import timeit
import random as rdm
start = timeit.default_timer()

#grafo vacio
grafo = {}

#lista de nodos posibles
listaNodos = [
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X','Y','Z',
            'A2','B2','C2','D2','E2','F2','G2','H2','I2','J2','K2','L2','M2','N2','O2','P2',
            'Q2','R2','S2','T2','U2','V2','W2','X2','Y2','Z2',
            'A3','B3','C3','D3','E3','F3','G3','H3','I3','J3','K3','L3','M3','N3','O3','P3',
            'Q3','R3','S3','T3','U3','V3','W3','X3','Y3','Z3',
            'A4','B4','C4','D4','E4','F4','G4','H4','I4','J4','K4','L4','M4','N4','O4','P4',
            'Q4','R4','S4','T4','U4','V4','W4','X4','Y4','Z4'
]

def dijkstra(grafo, inicial, final):
        INF = float('inf')
        sinVisitar = {nodo: INF for nodo in grafo.keys()}
        previo = {nodo: nodo for nodo in grafo.keys()} 
        visitado = {}
        actual = inicial
        pesoActual = 0
        sinVisitar[actual] = pesoActual
        while True:
            for nodo, peso in grafo[actual]:
                if nodo not in sinVisitar:
                    continue
                pesoNuevo = pesoActual + peso
                if sinVisitar[nodo] > pesoNuevo:
                    sinVisitar[nodo] = pesoNuevo
                    previo[nodo] = actual 
            visitado[actual] = pesoActual    
            sinVisitar.pop(actual)
            if not sinVisitar:
                break
            candidatos = [(n, s) for n, s in sinVisitar.items() if s != INF]
            actual, pesoActual = sorted(candidatos, key = lambda x: x[1])[0]
        camino = []
        nodo = final
        while True:
            camino.append(nodo)
            if(nodo == previo[nodo]):
                break
            nodo = previo[nodo]
        return (camino[::-1], visitado[final])

def a_star(grafo, inicial, final):
    
    def h(n):
        return 0
    
    frontera = PriorityQueue()
    frontera.put(inicial, 0)
    vino_de = {}
    peso_de_momento = {}
    vino_de[inicial] = None
    peso_de_momento[inicial] = 0

    while not frontera.empty():
        actual = frontera.get()

        if actual == final:
            break

        for nodo_sig, peso in grafo[actual]:
            nuevo_p = peso_de_momento[actual] + peso
            if nodo_sig not in peso_de_momento or nuevo_p < peso_de_momento[nodo_sig]:
                peso_de_momento[nodo_sig] = nuevo_p
                prioridad = nuevo_p + h(nodo_sig)
                frontera.put(nodo_sig, prioridad)
                vino_de[nodo_sig] = actual

    ruta = []
    actual = final
    while actual != inicial:
        ruta.append(actual)
        actual = vino_de[actual]
    ruta.append(inicial)
    ruta.reverse()

    return ruta, peso_de_momento[final]

def nuevoArco(grafo, arco, peso):
        n1, n2 = tuple(arco)
        for n, e in [(n1, n2), (n2, n1)]:
            if n in grafo:
                if e not in grafo[n]:
                    grafo[n].append((e, peso))
                    if n == e:
                        break
            else:
                grafo[n] = [(e, peso)]

def tam(grafo):
        return len(grafo)


#codigo para imprimir el grafo como lista

def existNode(grafo, node):
        return node in grafo.keys()

def edges(grafo, node=None):
        if node:
            if existNode(node):
                return [(node, e) for e in grafo[node]]
            else:
                return []
        else:
            return [(n, e) for n in grafo.keys() for e in grafo[n]]




def prueba(grafo, inicial, final):

    ruta, pesoTotal = dijkstra(grafo, inicial, final)
    print(f'La ruta mas corta encontrada es:{ruta} peso:{pesoTotal}')
    
def prueba2(grafo, inicial, final):
    ruta, pesoTotal = a_star(grafo, inicial, final)
    print(f'La ruta A* encontrada es:{ruta} peso:{pesoTotal}')

if __name__ == '__main__':

    
    e = rdm.randint(24,99)
    listaNodosRandom = listaNodos[0:e]

    inicial = rdm.choice(listaNodosRandom)
    listaSinInicial = [i for i in listaNodosRandom if i != inicial]
    final = rdm.choice(listaSinInicial)


    #grafo donde cada nodo tiene al menos tres arcos
    for i in listaNodosRandom:
        #lista donde no se puede hacer un arco de un nodo a si mismo
        listaNodosBuena = [j for j in listaNodosRandom if j != i]
        nuevoArco(grafo,(i, rdm.choice(listaNodosBuena)), rdm.randint(1,10)) #arco de entre 1 a 10 de peso
        nuevoArco(grafo,(i, rdm.choice(listaNodosBuena)), rdm.randint(1,10)) #arco de entre 1 a 10 de peso
        nuevoArco(grafo,(i, rdm.choice(listaNodosBuena)), rdm.randint(1,10)) #arco de entre 1 a 10 de peso
    
    grafo1 = {'A': [('B', 1), ('C', 2), ('D', 3),],
         'B': [('A', 1), ('C', 4),],
         'C': [('A', 2), ('B', 4), ('D', 5)],
         'D': [('A', 3), ('C', 5)]}
         
    inicial1 = 'A'
    
    print(tam(grafo)+1)
    start = timeit.default_timer()
    #print(edges(grafo)) #<-------------imprime lista del grafo random  (descomentar el codigo de arriba)
    prueba(grafo, inicial, final)
    end = timeit.default_timer()
    print("Terminado en --- %s segundos ---" % (end - start))
    start = timeit.default_timer()
    prueba2(grafo, inicial, final)
    end = timeit.default_timer()
    print("Terminado en --- %s segundos ---" % (end - start))