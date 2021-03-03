import random


def ordenamiento_por_insercion(lista):
    lista_ordenada = []
    lista_ordenada.append(lista.pop(0))

    for _ in range(len(lista)):
        valor_actual = lista.pop(0)
        for j in range(len(lista_ordenada)):
            if valor_actual <= lista_ordenada[j]:
                lista_ordenada.insert(j, valor_actual)
                break
            if valor_actual > lista_ordenada[-1]:
                lista_ordenada.append(valor_actual)
                break

    return lista_ordenada


if __name__ == '__main__':

    # tamano_de_lista = int(input('De que tamano sera la lista? '))
    tamano_de_lista = 10

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)
