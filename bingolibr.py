'''
Libreria de funciones para Bingo
'''
import random

class Carton:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.carton = [[random.randint(1, 99) for _ in range(columnas)] for _ in range(filas)]
        self.carton_mostrado = [['XX' for _ in range(columnas)] for _ in range(filas)]  # Inicialmente todos los números están ocultos

    def mostrar_carton(self):
        print("Estado actual del cartón:")
        for fila in self.carton_mostrado:
            print(" ".join(map(str, fila)))

    def sacar_bola(self):
        numero = random.randint(1, 99)
        print("Ha salido la bola número:", numero)
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.carton[i][j] == numero:
                    self.carton_mostrado[i][j] = numero
                    print("Número encontrado en el cartón:", numero)
        self.mostrar_carton()
