import random

# Matriz
matriz = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# Mostrar la matriz de manera cuadrada con números alineados
def Mostrar_Matriz():
    for fila in matriz:
        print("|", end=" ")
        for elemento in fila:
            # Imprimir cada número alineado a la izquierda dentro de un ancho calculado con el numero maximo de la matriz
            print(str(elemento).ljust(len(str(max(max(fila) for fila in matriz)))), end=" ")
        print("|")

def Verificar_Matriz_Llena():
    return not any(0 in fila for fila in matriz) #devuelve True si NO consigue un 0

def Verificar_Victoria(num):
    return any(num in fila for fila in matriz) #devuelve True si consigue el valor de la victoria

def Verificar_Si_Hay_Movimientos_Posibles():
    for i in range(4):
        for j in range(3):
            if matriz[i][j] == matriz[i][j+1]:
                return True
    for i in range(3):
        for j in range(4):
            if matriz[i][j] == matriz[i+1][j]:
                return True
    return False

def Agregar_Valor_Aleatorio():
    global eleccionJuego
    posiciones = []
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                posiciones.append((i, j))
    x, y = random.choice(posiciones)
    matriz[x][y] = eleccionJuego*random.randint(1, 2)


#mueve el tablero en la direccion desada mov=(izquierda, derecha, arriba, abajo)
def Mover_Tablero(mov):
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
                   

#solicita un numero del 1 al (fin), valida y retorna dicho numero
def Solicitar_numero(fin):
    opcion = input("Ingrese la opción que desea: ")
    while not opcion.isdigit() or not 1 <= int(opcion) <= fin:
        print("Opción inválida. Ingrese un mumero entre 1 y",fin,":")
        opcion = input("Ingrese la opción que desea: ")
    return opcion

def solicitar_letra(opciones):
    opcion = input("Ingrese la opción que desea: ").lower()
    while opcion not in opciones:
        print("Opción inválida. Ingrese una de las siguientes opciones:", ', '.join(opciones))
        opcion = input("Ingrese la opción que desea: ").lower()
    return opcion


# Declaracion de variables globales
puntos=0
eleccionJuego=0 #numero entre 1 y 10 para saber si juega 1024, 2048, 3072, etc
nombre_jugador=''#se declara global para guardarlo una sola vez

# funcion principal
def Main():
    global eleccionJuego
    global puntos
    global nombre_jugador
    victoriaAnunciada = False #para que solo le indique que gano una vez
    print("Bienvenido a N210 que desea hacer [ 1 - 5 ]")
    print("  [1]: Jugar N210.")
    print("  [2]: Continuar partida guardada.")
    print("  [3]: Mostrar ganadores.")
    print("  [4]: Mostrar puntajes.")
    print("  [5]: Salir")
    opcion=Solicitar_numero(5)
    if opcion == '1':
        print("Introduce N [ 1 - 10 ]:")
        eleccionJuego = int(Solicitar_numero(10))
        matriz[random.randint(0, 1)][random.randint(0, 1)]=eleccionJuego #colocar 2 numeros aleatorios en el tablero
        matriz[random.randint(2, 3)][random.randint(2, 3)]=eleccionJuego
        while True:
            print("su puntuacion es ",puntos,".   El objetivo es:",eleccionJuego*1024)
            Mostrar_Matriz()
            print("arriba [w], abajo [s], izquierda [a], derecha [d], guardar [g], salir [q]")
            movimiento=solicitar_letra(['w', 's', 'd', 'a','g','q'])
            if movimiento == 'a':
                Mover_Tablero('izquierda')
            elif movimiento == 'w':
                Mover_Tablero('arriba')
            elif movimiento == 's':
                Mover_Tablero('abajo')
            elif movimiento == 'd':
                Mover_Tablero('derecha')
            elif movimiento == 'g':
                print("no esta implementado el guardado")
            elif movimiento == 'q':
                print("Hasta pronto!!")
                break
            if movimiento in ['w', 's', 'd', 'a']:#si realizo un movimiento
                if not Verificar_Si_Hay_Movimientos_Posibles(): #verificar si perdio el juego
                    Mostrar_Matriz()
                    print("Fin del juego! su puntucacion total fue: ",puntos)
                    if nombre_jugador=='':
                        nombre_jugador = input("Ingrese su nombre:")
                    break
                if Verificar_Victoria(eleccionJuego*1024) and not victoriaAnunciada: #verificar victoria
                    victoriaAnunciada=True
                    print("Has ganado!!!!")
                    if nombre_jugador=='':
                        nombre_jugador = input("Ingrese su nombre:")
                    print("Felicidades",nombre_jugador,"!!! Deseas seguir jugando (sandbox)? si [s], no[n]:")
                    if solicitar_letra(['s', 'n'])=='n':
                        break
                if not Verificar_Matriz_Llena():
                    Agregar_Valor_Aleatorio()
                
    elif opcion == '2':
        print("Código para Continuar partida guardada.")
    elif opcion == '3':
        print("Código para Mostrar ganadores.")
    elif opcion == '4':
        print("Código para Mostrar puntajes.")
    elif opcion == '5':
        print("Código para Salir")

Main()