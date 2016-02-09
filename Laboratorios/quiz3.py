#programa que maneje una lista supermercado donde puedes agregar , ver,
# buscar y eliminar articulos los articulos estan en una tupla arroz,leche,tuna,cereal,jugo#
def imprimi(articulos):
    print("articulos:")
    for k, v in articulos.items():
        print("Articulo:",k)
    print()
def agregar(articulos,articulo):
    articulos[articulo]=articulo

def borrar(articulos, nombre):
    if nombre in articulos:
        del articulos[nombre]
    else:
        print(nombre," no hay articulo en la lista.")
lista_de_tupla= ("1- arroz","2- leche","3-tuna","4- cereal","5- jugo")
def menu():

    print('1. Agregar articulo')
    print('2. Eliminar articulo')
    print('3. Ver lista')
    print('4. Salir')

if __name__ == '__main__':
    lista_de_articulos = {}
    opcion_menu = 0
    while True:
        menu()
        try:
            opcion_menu = int(input("¿Que opción escoges?: "))
        except:
            print("Opcion no valida")
        else:
            if opcion_menu == 1:
                 print("Agregar Articulo")
                 print("Articulos disponibles")
                 print(lista_de_tupla)
                 nombre = input("articulo: ")
                 agregar(lista_de_articulos, nombre)

            elif opcion_menu == 2:
                print("Eliminar articulo")
                imprimi(lista_de_articulos)
                nombre = input("Articulo: ")
                borrar(lista_de_articulos, nombre)
            elif opcion_menu == 3:
                print("ver lista")
                imprimi(lista_de_articulos)
