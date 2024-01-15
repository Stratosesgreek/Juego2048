# Matriz
matriz = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# Matriz del 1 al 16
matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

matriz = [[2, 2, 2, 2],
          [0, 0, 4, 4],
          [4, 0,  0, 4],
          [16, 0, 4, 16]]

matriz = [[2, 4, 8, 16],
          [32, 64, 128, 256],
          [512, 1024, 2048, 4096],
          [8192, 16384, 32768, 65536]]

matriz = [[2, 4, 8, 16],
          [32, 64, 128, 256],
          [512, 1024, 2048, 4096],
          [8192, 16384, 32768, 32768]]



puntos=0

# Mostrar la matriz de manera cuadrada con números alineados
def MostrarMatriz():
    for fila in matriz:
        print("|", end=" ")
        for elemento in fila:
            # Imprimir cada número alineado a la izquierda dentro de un ancho calculado con el numero maximo de la matriz
            print(str(elemento).ljust(len(str(max(max(fila) for fila in matriz)))), end=" ")
        print("|")

def VerificarMatrizLlena():
    return not any(0 in fila for fila in matriz) #devuelve True si NO consigue un 0

def VerificarVictoria(num):
    return any(num in fila for fila in matriz) #devuelve True si no consigue un 0


def VerificarSiHayMovimientosPosibles():
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == matriz[i + 1][j+1]:
                return True
    for i in range(3):
        for j in range(3):
            if matriz[j][i] == matriz[j + 1][i+1]:
                return True
    return False


def Movimiento(mov):
    global puntos
    for i in range(4):
        numeros=[]
        for j in range(4):
            if mov=='izquierda' or mov=='derecha':
                numeros.append(matriz[i][j]) if matriz[i][j]!=0 else None
            else:
                numeros.append(matriz[j][i]) if matriz[j][i]!=0 else None
        for k in range(len(numeros)-1):
            if numeros[k]==numeros[k+1]:
                numeros[k]*=2
                numeros[k+1]=0
                puntos+=(numeros[k])
        while 0 in numeros:
            numeros.remove(0)
        while len(numeros)<4:
            if mov=='arriba' or mov=='izquierda':
                numeros.append(0)
            else:
                numeros.insert(0,0)
        for l in range(4):
            if mov=='izquierda' or mov=='derecha':
                matriz[i][l]=numeros[l]
            else:
                matriz[l][i]=numeros[l]
                   
#Movimiento('izquierda')
MostrarMatriz()
print(puntos)
print(VerificarMatrizLlena())
print(VerificarVictoria(1024))
print(VerificarSiHayMovimientosPosibles())