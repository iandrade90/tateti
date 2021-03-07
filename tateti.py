from os import system

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]



class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def bienvenido(self):
        return 'Bienvenid@ {} al juego'.format(self.nombre)

def matriz_creador(n):
    for i in n:
        for x in i:
            print(x, '', '', end='')
        print()
        print()

def juego():
    print('Bienvenido a Ta Te Ti!!!!!')
    print()
    
    print('Les presentamos el tablero de juego, deben seleccionar su movimiento al ingresar el numero dentro del cuadrante deseado.')
    print('Las reglas son las reglas basicas del Ta Te Ti')
    print('Las x siempre mueven primero.')
    print('Suerte!!')
    print()

def dinamica():

    while True:


        seleccionX = int(input('{} indica tu movimiento: '.format(jugador1.nombre)))

        for x, row in enumerate(matriz):
            for y, element in enumerate(row):
                if element == seleccionX:
                    matriz[x][y] = 'X' 

        system('clear')
        matriz_creador(matriz)

        if type(matriz[0][0]) == str and type(matriz[0][1]) == str and type(matriz[0][2]) == str:
            if type(matriz[1][0]) == str and type(matriz[1][1]) == str and type(matriz[1][2]) == str:
                if type(matriz[2][0]) == str and type(matriz[2][1]) == str and type(matriz[2][2]) == str:
                    print('Juego empatado!')
                    break

        matrizPlana = [x for i in matriz for x in i]

        if matrizPlana[0] == 'X' and matrizPlana[1] == 'X' and matrizPlana[2] == 'X':
            print('{} has ganado el juego!'.format(jugador1.nombre))
            break
        elif matrizPlana[3] == 'X' and matrizPlana[4] == 'X' and matrizPlana[5] == 'X':
            print('{} has ganado el juego!'.format(jugador1.nombre))
            break
        elif matrizPlana[6] == 'X' and matrizPlana[7] == 'X' and matrizPlana[8] == 'X':
            print('{} has ganado el juego!'.format(jugador1.nombre))
            break
        elif matrizPlana[0] == 'X' and matrizPlana[3] == 'X' and matrizPlana[6] == 'X':
            print('{} has ganado el juego!'.format(jugador1.nombre))
            break
        elif matrizPlana[1] == 'X' and matrizPlana[4] == 'X' and matrizPlana[7] == 'X':
            print('{} has ganado el juego!'.format(jugador1.nombre))
            break
        elif matrizPlana[2] == 'X' and matrizPlana[5] == 'X' and matrizPlana[8] == 'X':
            print('{} has ganado el juego!'.format(jugador1.nombre))
            break
        elif matrizPlana[0] == 'X' and matrizPlana[4] == 'X' and matrizPlana[8] == 'X':
            print('{} has ganado el juego!'.format(jugador1.nombre))
            break
        elif matrizPlana[2] == 'X' and matrizPlana[4] == 'X' and matrizPlana[6] == 'X':
            print('{} has ganado el juego!'.format(jugador1.nombre))
            break
        else:
            print('No hay ganador todavia, el juego continua')
            seleccionO = int(input('{} indica tu movimiento: '.format(jugador2.nombre)))

        for x, row in enumerate(matriz):
            for y, element in enumerate(row):
                if element == seleccionO:
                    matriz[x][y] = 'O'

        system('clear')
        matriz_creador(matriz) 
        matrizPlana = [x for i in matriz for x in i]

        if matrizPlana[0] == 'O' and matrizPlana[1] == 'O' and matrizPlana[2] == 'O':
            print('{} has ganado el juego!'.format(jugador2.nombre))
            break
        elif matrizPlana[3] == 'O' and matrizPlana[4] == 'O' and matrizPlana[5] == 'O':
            print('{} has ganado el juego!'.format(jugador2.nombre))
            break
        elif matrizPlana[6] == 'O' and matrizPlana[7] == 'O' and matrizPlana[8] == 'O':
            print('{} has ganado el juego!'.format(jugador2.nombre))
            break
        elif matrizPlana[0] == 'O' and matrizPlana[3] == 'O' and matrizPlana[6] == 'O':
            print('{} has ganado el juego!'.format(jugador2.nombre))
            break
        elif matrizPlana[1] == 'O' and matrizPlana[4] == 'O' and matrizPlana[7] == 'O':
            print('{} has ganado el juego!'.format(jugador2.nombre))
            break
        elif matrizPlana[2] == 'O' and matrizPlana[5] == 'O' and matrizPlana[8] == 'O':
            print('{} has ganado el juego!'.format(jugador2.nombre))
            break
        elif matrizPlana[0] == 'O' and matrizPlana[4] == 'O' and matrizPlana[8] == 'O':
            print('{} has ganado el juego!'.format(jugador2.nombre))
            break
        elif matrizPlana[2] == 'O' and matrizPlana[4] == 'O' and matrizPlana[6] == 'O':
            print('{} has ganado el juego!'.format(jugador2.nombre))
            break
        else:
            print('No hay ganador todavia, el juego continua') 


juego()

jugador1 = Jugador(input('Hola jugador X, Cual es tu nombre?: '))
jugador2 = Jugador(input('Hola jugador O, Cual es tu nombre?: '))

print()

print(jugador1.bienvenido())
print(jugador2.bienvenido())
print()



matriz_creador(matriz)

dinamica()
