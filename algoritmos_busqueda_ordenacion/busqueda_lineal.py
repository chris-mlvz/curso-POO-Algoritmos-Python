import random


def busqueda_lineal(lista, objetivo, iter_cuenta=0):
    match = False

    for elemento in lista:
        iter_cuenta += 1
        if elemento == objetivo:
            match = True
            break
    return (match, iter_cuenta)


if __name__ == '__main__':
    tamamo_de_lista=int(input('De que tamano sera la lista? '))
    objetivo=int(input('Que numero quieres encontrar '))

    lista=[random.randint(0, 100) for i in range(tamamo_de_lista)]

    (encontrado, iter_cuenta)=busqueda_lineal(lista, objetivo)
    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Número de iteraiones: {iter_cuenta}')
