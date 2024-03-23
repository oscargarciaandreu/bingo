'''
Este codigo recrea el juego del Bingo
'''
from bingolibr import Carton

def menu_principal():
    print("Bienvenido al juego de Bingo modificado")
    print("1. Crear cartón")
    print("2. Mostrar cartón")
    print("3. Sacar bola")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    opcion = ''
    carton = None
    while opcion != '4':
        opcion = menu_principal()
        if opcion == '1':
            filas = int(input("Ingrese el número de filas del cartón: "))
            columnas = int(input("Ingrese el número de columnas del cartón: "))
            carton = Carton(filas, columnas)
        elif opcion == '2':
            if carton:
                carton.mostrar_carton()
            else:
                print("Primero debe crear un cartón.")
        elif opcion == '3':
            if carton:
                carton.sacar_bola()
            else:
                print("Primero debe crear un cartón.")
        elif opcion == '4':
            print("Gracias por jugar al Bingo modificado.")

if __name__ == "__main__":
    main()
